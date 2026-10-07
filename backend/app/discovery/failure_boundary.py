class FailureBoundaryEstimator:
    def __init__(self):
        self.points = []

    def add_point(self, severity: float, failure: bool):
        self.points.append((severity, failure))

    def estimate_boundary(self) -> float:
        if not self.points:
            return 0.5
        # Simple heuristic: average of highest success and lowest failure
        successes = [p[0] for p in self.points if not p[1]]
        failures = [p[0] for p in self.points if p[1]]
        if successes and failures:
            return (max(successes) + min(failures)) / 2.0
        return 0.5
