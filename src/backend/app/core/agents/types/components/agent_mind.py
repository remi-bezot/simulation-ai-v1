from typing import Dict, Optional
from app.core.agents.types.components.emotions import Emotions
from app.core.agents.types.components.needs import Needs
from app.core.agents.types.components.state import State
from app.core.agents.types.interfaces.i_agent_mind import IAgentMind


class AgentMind(IAgentMind):
    def __init__(self):
        self.emotions = Emotions()
        self.needs = Needs()
        self.state = State()
        self.aspiration: Optional[str] = None
        self.experience = 0

    def update(self) -> None:
        """
        Met à jour l'état mental de l'agent.
        """
        self.emotions.decay()
        self.needs.update()
        self.state.update_mood(self.emotions.get_mood())

    def feel_emotion(self, emotion: str, intensity: float) -> Optional[bool]:
        """
        Ressent une émotion.

        :param emotion: Le type d'émotion ressenti.
        :param intensity: L'intensité de l'émotion.
        :return: True si l'émotion est ressentie, False sinon.
        """
        return self.emotions.feel(emotion, intensity)

    def satisfy_need(self, need: str, amount: float) -> Optional[float]:
        """
        Satisfait un besoin.

        :return: Quantité satisfaite ou None si le besoin n'existe pas
        """
        try:
            self.needs.satisfy_need(need, amount)
            return amount
        except KeyError:
            return None

    def set_aspiration(self, aspiration: Optional[str]) -> bool:
        """
        Définit une aspiration.

        :param aspiration: La nouvelle aspiration ou None pour effacer
        :return: True si l'aspiration est définie, False sinon
        """
        try:
            self.aspiration = aspiration
            return True
        except Exception:
            return False

    def get_current_state(self) -> Dict[str, Optional[float]]:
        """
        Retourne l'état mental actuel.

        :return: Dictionnaire avec les états et leurs valeurs
        """
        return {
            "emotions": self.emotions.get_current(),
            "needs": self.needs.get_current(),
            "state": self.state.get_current(),
            "aspiration": self.aspiration,
            "experience": self.experience,
        }

    def gain_experience(self, amount: float) -> None:
        """Gagne de l'expérience"""
        self.experience += amount
