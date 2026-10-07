from app.api.schemas import Trace

class TraceCollector:
    def __init__(self):
        self.traces = []

    def collect(self, trace: Trace):
        self.traces.append(trace)
