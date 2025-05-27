from ultralytics import YOLO

def main():
    model = YOLO("yolov8x.pt")
    model.train(
        data="data.yaml",
        epochs=50,  
        imgsz=640,
        batch=14,  
        device=0,
        amp=True, 
        workers=8,

        lr0=0.005,
        lrf=0.1,
        momentum=0.937,
        weight_decay=0.0005,
        warmup_epochs=5,
        warmup_momentum=0.8,
        warmup_bias_lr=0.1,
        cos_lr=True,

        augment=True,
        mosaic=0.8,
        mixup=0.3,
        hsv_h=0.015,
        hsv_s=0.7,
        hsv_v=0.4,
        translate=0.1,
        scale=0.5,
        fliplr=0.5,
        flipud=0.0,
        
        patience=15, 
        save_period=1,
        cache="disk",
        plots=True
    )


if __name__ == '__main__':
    main()
