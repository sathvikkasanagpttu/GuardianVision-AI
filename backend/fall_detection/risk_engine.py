from dataclasses import dataclass

@dataclass
class RiskResult:
    score: float
    state: str
    reasons: list

class FallRiskEngine:
    def __init__(self, threshold=0.80):
        self.threshold = threshold

    def score(self, aspect_ratio=0.5, torso_angle=35,
              vertical_velocity=0, ground_proximity=0,
              pose_confidence=0.9, persistence=0):
        horizontal = min(1, max(0, (aspect_ratio-0.9)/1.5))
        torso = min(1, max(0, (torso_angle-55)/55))
        velocity = min(1, abs(vertical_velocity)/25)
        ground = min(1, max(0, ground_proximity))
        persist = min(1, persistence)
        score = (0.24*horizontal + 0.24*torso + 0.22*velocity +
                 0.15*ground + 0.05*pose_confidence + 0.10*persist)
        score = max(0, min(1, score))
        if score >= self.threshold: state = "FALL CONFIRMED"
        elif score >= 0.60: state = "POSSIBLE FALL"
        elif score >= 0.30: state = "MONITOR"
        else: state = "NORMAL"
        reasons = []
        if horizontal > 0.6: reasons.append("horizontal body geometry")
        if torso > 0.6: reasons.append("large torso-angle change")
        if velocity > 0.6: reasons.append("rapid vertical movement")
        if ground > 0.6: reasons.append("near-ground posture")
        return RiskResult(round(score, 3), state, reasons)
