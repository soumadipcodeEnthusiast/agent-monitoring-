from app.discovery.strategies.adaptive import AdaptiveStrategy

class AdaptiveSelector:
    def __init__(self):
        self.strategy = AdaptiveStrategy()
        
    def select(self, state: dict):
        return self.strategy.select_next_experiment(state)
