import os, time, cv2

class IncidentRecorder:
    def __init__(self, directory="../incidents"):
        self.directory = directory
        os.makedirs(directory, exist_ok=True)

    def save_snapshot(self, frame, prefix="fall"):
        path = os.path.join(self.directory, f"{prefix}_{int(time.time())}.jpg")
        cv2.imwrite(path, frame)
        return path
