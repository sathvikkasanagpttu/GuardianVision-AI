from backend.fall_detection.risk_engine import FallRiskEngine
def test_score_range():
    r = FallRiskEngine().score()
    assert 0 <= r.score <= 1
