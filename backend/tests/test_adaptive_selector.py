from app.discovery.adaptive_selector import AdaptiveSelector

def test_adaptive_selector():
    selector = AdaptiveSelector()
    res = selector.select({})
    assert "severity" in res
