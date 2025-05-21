from ultralytics import YOLO
import torch

# Очистка памяти GPU перед запуском
torch.cuda.empty_cache()

# Загрузка вашей обученной модели
model = YOLO("runs/detect/weed_v3_final/weights/best.pt")

# Параметры для экономии памяти
results = model.predict(
    source="C:\yolo_project\screen",
    imgsz=320,        
    batch=2,          
    conf=0.4,         
    device="0",       
    half=True,        
    save=True,
    save_txt=True,
    project="weed_results",
    name="final_run"
)


torch.cuda.empty_cache()