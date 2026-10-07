from app.discovery.adaptive_selector import AdaptiveSelector

class AdaptiveDiscoveryEngine:
    def __init__(self):
        self.selector = AdaptiveSelector()

    async def propose_experiment(self, state: dict):
        return self.selector.select(state)

    async def record_result(self, result: dict):
        pass

    async def update_model(self):
        pass
