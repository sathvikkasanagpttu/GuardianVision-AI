import mediapipe as mp

class PoseEstimator:
    def __init__(self):
        self.pose = mp.solutions.pose.Pose(
            static_image_mode=False, model_complexity=1,
            enable_segmentation=False,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5)

    def estimate(self, frame):
        rgb = frame[:, :, ::-1]
        return self.pose.process(rgb).pose_landmarks
