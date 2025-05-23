from dataclasses import dataclass
from PIL.Image import Image
from torch.types import Tensor
from ultralytics import YOLO

@dataclass
class ProcessedImage():
    image : Image
    boxes : list[Tensor]


def process_image(image : str | Image) -> ProcessedImage:
    model = YOLO("Project/UI/model.pt")  # pretrained YOLO11n model
    results = model(image)

    boxes = []
    for result in results:
        for box in result.boxes:
            boxes.append(box.xywh[0].to("cpu"))
        image = result

    return ProcessedImage(image, boxes)
