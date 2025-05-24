from ultralytics import YOLO
import torch

# Очистка памяти GPU перед запуском
torch.cuda.empty_cache()

# Загрузка вашей обученной модели
from ultralytics import YOLO

model = YOLO("runs/detect/weed_4080_v1/weights/best.pt")
results = model.predict(
    source="C:\yolo_project\screen",
    imgsz=640,
    conf=0.4,
    device=0,
    half=True,
    fuse=True,	
    save=True,
    project="weed_results",
    name="final_run",
    exist_ok=True
)

torch.cuda.empty_cache()
