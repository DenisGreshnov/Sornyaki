from ultralytics import YOLO

model = YOLO("yolov8x.pt")  
model.train(
    data="data.yaml",        
    epochs=300,
    imgsz=640,
    batch=24,               
    device=0,
    amp=True,
    workers=8,  
    lr0=0.001,
    cos_lr=True,
    cache="disk",
    plots=True   
)
