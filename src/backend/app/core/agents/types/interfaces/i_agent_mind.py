from abc import ABC, abstractmethod
from typing import Dict, Optional


class IAgentMind(ABC):
    """Interface pour l'esprit d'un agent."""

    @abstractmethod
    def update(self) -> None:
        """
        Met à jour l'état mental de l'agent.
        """
        pass

    @abstractmethod
    def feel_emotion(self, emotion: str, intensity: float) -> Optional[bool]:
        """
        Ressent une émotion.

        :param emotion: Le type d'émotion ressenti.
        :param intensity: L'intensité de l'émotion.
        :return: True si l'émotion est ressentie, False si échec, None si impossible
        """
        pass

    @abstractmethod
    def satisfy_need(self, need: str, amount: float) -> Optional[float]:
        """
        Satisfait un besoin.

        :param need: Le type de besoin à satisfaire.
        :param amount: La quantité pour satisfaire le besoin.
        :return: La nouvelle valeur du besoin satisfait, None si impossible
        """
        pass

    @abstractmethod
    def set_aspiration(self, aspiration: Optional[str]) -> bool:
        """
        Définit une aspiration.

        :param aspiration: La nouvelle aspiration ou None pour effacer
        :return: True si l'aspiration est définie, False sinon
        """
        pass

    @abstractmethod
    def get_current_state(self) -> Dict[str, Optional[float]]:
        """
        Retourne l'état mental actuel.

        :return: Dictionnaire avec les états et leurs valeurs (None si non défini)
        """
        pass

    @abstractmethod
    def gain_experience(self, amount: float) -> None:
        """Gagne de l'expérience."""
        pass
