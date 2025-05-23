import cv2
import numpy as np

image = cv2.imread("Test.jpg")  # замените на путь к вашей фотографии
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Диапазон для зелёного
lower_green = np.array([35, 40, 40])
upper_green = np.array([85, 255, 255])

# Бинарная маска зелёного цвета
green_mask = cv2.inRange(hsv, lower_green, upper_green)

# Визуализация
cv2.imshow("Зелёная маска без табака", green_mask)
cv2.waitKey(0)
