from ultralytics import YOLO
import cv2

class ObjectDetector:
    def __init__(self, model_path="yolov8n.pt", conf_threshold=0.5):
        """Initializes the lightweight YOLOv8 model for real-time inference."""
        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold

    def detect(self, frame):
        """Runs object detection on a given frame and returns detection results."""
        results = self.model(frame, conf=self.conf_threshold, verbose=False)[0]
        detections = []

        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls_id = int(box.cls[0])
            label = self.model.names[cls_id]
            confidence = float(box.conf[0])

            detections.append({
                "label": label,
                "confidence": confidence,
                "bbox": (x1, y1, x2, y2),
                "center": ((x1 + x2) // 2, (y1 + y2) // 2)
            })

        return detections, results.plot()
