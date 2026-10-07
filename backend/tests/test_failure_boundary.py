from app.discovery.failure_boundary import FailureBoundaryEstimator

def test_boundary():
    est = FailureBoundaryEstimator()
    est.add_point(0.2, False)
    est.add_point(0.8, True)
    assert est.estimate_boundary() == 0.5
