from ultralytics import YOLO

model = YOLO("yolov8n.pt")  

model.train(
    data="data.yaml",
    epochs=500,
    imgsz=320,
    batch=16,
    workers=0,
    lr0=0.001,
    weight_decay=0.0005,
    patience=200,
    augment=True,
    hsv_h=0.2,
    hsv_s=0.6,
    degrees=15,
    flipud=0.1,
    name="weed_v3_final"
)
