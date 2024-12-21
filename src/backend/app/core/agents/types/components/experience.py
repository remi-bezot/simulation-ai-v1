class Experience:
    """Classe pour gérer l'expérience de l'agent"""

    def __init__(self):
        self.current = 0
        self.level = 1

    def gain(self, amount: float) -> None:
        """Gagne de l'expérience"""
        self.current += amount
        self.check_level_up()

    def check_level_up(self) -> None:
        """Vérifie si l'agent peut monter de niveau"""
        exp_needed = self.level * 100
        if self.current >= exp_needed:
            self.level_up()

    def level_up(self) -> None:
        """Monte de niveau"""
        self.level += 1
        self.current = 0
