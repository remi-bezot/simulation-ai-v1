from typing import Dict, List
from app.core.agents.exceptions.agent_exceptions import AgentDeadException
from app.core.agents.stats.history import HistoryTracker
from app.core.agents.types.components.needs import Needs
from app.core.agents.types.components.emotions import Emotions
from app.core.components.state import State


class StatusManager:
    """
    Gère les statuts de l'agent.
    """

    def __init__(self):
        self.status_effects: Dict[str, float] = {}
        self.needs = Needs()
        self.emotions = Emotions()
        self.stats = {
            "health": 100,
            "morale": 100,
        }

    def update_status(self, delta_time: float):
        """
        Met à jour tous les statuts de l'agent.

        :param delta_time: Le temps écoulé depuis la dernière mise à jour.
        """
        self.update_needs(delta_time)
        self.update_emotions(delta_time)
        self.update_effects(delta_time)
        self.check_thresholds()
        self.record_status()

    def update_needs(self, delta_time: float):
        """
        Met à jour les besoins.

        :param delta_time: Le temps écoulé depuis la dernière mise à jour.
        """
        self.needs.update(delta_time)
        if self.needs.is_critical():
            self.stats["health"] -= delta_time * 0.1

    def update_emotions(self, delta_time: float):
        """
        Met à jour les émotions.

        :param delta_time: Le temps écoulé depuis la dernière mise à jour.
        """
        self.emotions.decay(delta_time)
        self.stats["morale"] = self.emotions.get_mood()

    def update_effects(self, delta_time: float):
        """
        Met à jour les effets de statuts.

        :param delta_time: Le temps écoulé depuis la dernière mise à jour.
        """
        for effect, duration in list(self.status_effects.items()):
            self.status_effects[effect] -= delta_time
            if self.status_effects[effect] <= 0:
                del self.status_effects[effect]

    def check_thresholds(self):
        """
        Vérifie les seuils critiques.
        """
        if self.stats["health"] <= 0:
            raise AgentDeadException("L'agent est mort.")
        if self.stats["morale"] <= 0:
            self.stats["morale"] = 0

    def record_status(self):
        """
        Enregistre l'état actuel de l'agent.
        """
        HistoryTracker.record(self.stats)
