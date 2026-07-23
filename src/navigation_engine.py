class NavigationEngine:
    def __init__(self, frame_width=640, safe_distance_threshold=1.5):
        self.frame_width = frame_width
        self.safe_distance_threshold = safe_distance_threshold

    def get_spatial_zone(self, center_x):
        """Determines whether the obstacle is on the Left, Center, or Right."""
        third = self.frame_width / 3
        if center_x < third:
            return "Left"
        elif center_x < 2 * third:
            return "Center"
        else:
            return "Right"

    def analyze_hazards(self, detections, distance_estimator):
        """Generates real-time audio navigation commands based on spatial proximity."""
        alerts = []

        for det in detections:
            bbox = det["bbox"]
            bbox_width = bbox[2] - bbox[0]
            distance = distance_estimator.estimate_distance(bbox_width)
            zone = self.get_spatial_zone(det["center"][0])

            if distance < self.safe_distance_threshold:
                alerts.append(f"Warning: {det['label']} detected on your {zone}, {distance} meters away.")

        return alerts
