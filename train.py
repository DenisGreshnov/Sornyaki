from ultralytics import YOLO

model = YOLO("yolo11n.pt")
results = model.train(data="data10/data.yaml", epochs=100, imgsz=640)
