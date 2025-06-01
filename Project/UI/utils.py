import cv2
import numpy as np
from ultralytics import YOLO


def process_image(image_path, processed_path, masked_path, dots_path) -> list:
    model = YOLO("Project/UI/model.pt")

    image = cv2.imread(image_path)
    # image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = model(image)[0]
    results.save(processed_path)

    mask_tobacco = np.zeros(image.shape[:2], dtype=np.uint8)

    mean_squre = 0
    count = 0

    for box, cls in zip(results.boxes.xyxy, results.boxes.cls):
        class_name = model.names[int(cls)]

        if "tobacco" in class_name.lower():
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(mask_tobacco, (x1, y1), (x2, y2), 255, -1)
            mean_squre += 2 * (abs(x1 - x2) + abs(y1 - y2))
            count+=1

    mean_squre /= count
    mean_squre = int(mean_squre)


    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])

    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    green_mask[mask_tobacco == 255] = 0

    cv2.imwrite(masked_path, green_mask)

    weed_clusters = []
    contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 50 and area < mean_squre: #Настраиваемый параметр
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                weed_clusters.append((cx, cy))
                cv2.circle(image, (cx, cy), 5, (0, 0, 255), -1) #Рисует точки красным на изначальном изображении

    #Координаты центров скоплений сорняков"
    print(weed_clusters)

    cv2.imwrite(dots_path, image)
    return weed_clusters
