class Energy:
    """Classe pour gérer l'énergie de l'agent"""

    def __init__(self, initial: float, maximum: float):
        self.current = initial
        self.maximum = maximum

    def modify(self, amount: float) -> bool:
        """Modifie l'énergie"""
        new_energy = self.current + amount
        if new_energy >= 0:
            self.current = min(self.maximum, new_energy)
            return True
        return False
