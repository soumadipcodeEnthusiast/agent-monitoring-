from app.discovery.hypothesis import Hypothesis

def test_hypothesis():
    h = Hypothesis(id="1", description="test", category="test", confidence=0.9)
    assert h.status == "PROPOSED"
