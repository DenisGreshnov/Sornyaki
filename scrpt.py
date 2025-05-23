import cv2
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description='Создание скриншотов каждой секунды видео')
    parser.add_argument('video_path', help='Путь к видеофайлу')
    parser.add_argument('output_dir', help='Папка для сохранения скриншотов')
    args = parser.parse_args()

    # Создаем папку для результатов
    os.makedirs(args.output_dir, exist_ok=True)

    # Открываем видео
    cap = cv2.VideoCapture(args.video_path)
    if not cap.isOpened():
        print("Ошибка: не удалось открыть видеофайл")
        return

    # Получаем параметры видео
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        print("Ошибка: неверный FPS видео")
        return

    frame_count = 0
    target_second = 0

    print("Обработка видео...")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Рассчитываем текущее время в секундах
        current_time = frame_count / fps
        frame_count += 1

        if current_time >= target_second:
            # Сохраняем кадр
            output_path = os.path.join(args.output_dir, f"second_{target_second}.jpg")
            if cv2.imwrite(output_path, frame):
                print(f"Сохранен скриншот для {target_second} секунды")
            else:
                print(f"Ошибка сохранения для {target_second} секунды")
            target_second += 1

    cap.release()
    print(f"Готово! Сохранено скриншотов: {target_second}")

if __name__ == "__main__":
    main()