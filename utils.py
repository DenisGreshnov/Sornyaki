from PIL.Image import Image
from torch.types import Tensor
from ultralytics import YOLO


def get_boxes_xywh(image : Image) -> list[Tensor]:
    res = []

    model = YOLO("best.pt")  # pretrained YOLO11n model
    results = model(image)

    for result in results:
        for box in result.boxes:
            res.append(box.xywh[0].to("cpu"))

    return res
