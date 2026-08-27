from collections import deque

class TemporalAnalyzer:
    def __init__(self, window=20, confirmation_frames=8, threshold=0.80):
        self.values = deque(maxlen=window)
        self.confirmation_frames = confirmation_frames
        self.threshold = threshold

    def update(self, risk_score):
        self.values.append(risk_score)
        recent = list(self.values)[-self.confirmation_frames:]
        return len(recent) == self.confirmation_frames and all(v >= self.threshold for v in recent)
