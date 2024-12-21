class Health:
    """Classe pour gérer la santé de l'agent"""

    def __init__(self, initial: float, maximum: float):
        self.current = initial
        self.maximum = maximum

    def modify(self, amount: float) -> None:
        """Modifie les points de vie"""
        self.current = max(0, min(self.maximum, self.current + amount))

    def is_alive(self) -> bool:
        """Vérifie si l'agent est en vie"""
        return self.current > 0
