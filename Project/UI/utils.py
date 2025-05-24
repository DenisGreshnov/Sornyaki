import cv2
import numpy as np
from ultralytics import YOLO


def process_image(image_path, processed_path, masked_path) -> None:
    model = YOLO("Project/UI/model.pt")

    image = cv2.imread(image_path)
    # image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = model(image)[0]
    results.save(processed_path)

    mask_tobacco = np.zeros(image.shape[:2], dtype=np.uint8)

    for box, cls in zip(results.boxes.xyxy, results.boxes.cls):
        class_name = model.names[int(cls)]

        if "tobacco" in class_name.lower():
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(mask_tobacco, (x1, y1), (x2, y2), 255, -1)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])

    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    green_mask[mask_tobacco == 255] = 0

    cv2.imwrite(masked_path, green_mask)
    return
