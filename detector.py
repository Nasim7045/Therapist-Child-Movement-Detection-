# scripts/detector.py
import torch

class Detector:
    def __init__(self, model_path='yolov5s'):
        self.model = torch.hub.load('ultralytics/yolov5', model_path)

    def detect(self, frame):
        results = self.model(frame)
        detections = results.xyxy[0].cpu().numpy()  # xyxy format
        return detections

