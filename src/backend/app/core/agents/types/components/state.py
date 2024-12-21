class State:
    """Classe pour gérer l'état général de l'agent"""

    def __init__(self):
        self.mood = "Neutral"

    def update_mood(self, mood: str) -> None:
        """Met à jour l'humeur"""
        self.mood = mood

    def get_current(self) -> str:
        """Retourne l'état actuel"""
        return self.mood
