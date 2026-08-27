class SimpleTracker:
    def update(self, detections):
        return [{**d, "track_id": i + 1} for i, d in enumerate(detections)]
