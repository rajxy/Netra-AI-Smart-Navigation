class DistanceEstimator:
    def __init__(self, focal_length=600, known_width=0.5):
        """
        focal_length: Calibrated camera focal length in pixels.
        known_width: Average real-world object width in meters (e.g., person/chair ~0.5m).
        """
        self.focal_length = focal_length
        self.known_width = known_width

    def estimate_distance(self, bbox_width):
        """
        Estimates real-world distance (in meters) using visual angle trigonometry:
        Distance = (Known Width * Focal Length) / Apparent Bounding Box Width
        """
        if bbox_width <= 0:
            return float('inf')
        distance = (self.known_width * self.focal_length) / bbox_width
        return round(distance, 2)
