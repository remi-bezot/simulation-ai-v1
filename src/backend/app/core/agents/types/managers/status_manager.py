from typing import Dict, List
from app.core.components.emotions import Emotions
from app.core.components.needs import Needs
from app.core.components.state import State


class AgentStatusManager:
    def __init__(self):
        self.emotions = Emotions()
        self.needs = Needs()
        self.state = State()
        self.stats = {"health": 100, "energy": 100, "morale": 100}
        self.status_history: List[Dict] = []
        self.status_effects: Dict[str, float] = {}

    def update_status(self, delta_time: float):
        """Met à jour tous les status de l'agent"""
        self.update_needs(delta_time)
        self.update_emotions(delta_time)
        self.update_effects(delta_time)
        self.check_thresholds()
        self.record_status()

    def update_needs(self, delta_time: float):
        """Met à jour les besoins"""
        self.needs.update(delta_time)
        if self.needs.is_critical():
            self.stats["health"] -= delta_time * 0.1

    def update_emotions(self, delta_time: float):
        """Met à jour les émotions"""
        self.emotions.decay(delta_time)
        self.stats["morale"] = self.emotions.get_mood()

    def update_effects(self, delta_time: float):
        """Met à jour les effets de status"""
        for effect, duration in list(self.status_effects.items()):
            self.status_effects[effect] -= delta_time
            if self.status_effects[effect] <= 0:
                del self.status_effects[effect]

    def check_thresholds(self):
        """Vérifie les seuils critiques"""
        for stat in self.stats:
            self.stats[stat] = max(0, min(100, self.stats[stat]))

    def add_effect(self, effect: str, duration: float):
        """Ajoute un effet de status"""
        self.status_effects[effect] = duration

    def has_effect(self, effect: str) -> bool:
        """Vérifie si un effet est actif"""
        return effect in self.status_effects

    def record_status(self):
        """Enregistre l'état actuel dans l'historique"""
        current_status = self.get_status()
        self.status_history.append(current_status)
        if len(self.status_history) > 100:
            self.status_history.pop(0)

    def get_status(self) -> dict:
        """Retourne le status complet"""
        return {
            "emotions": self.emotions.get_current(),
            "needs": self.needs.get_current(),
            "state": self.state.get_current(),
            "stats": self.stats.copy(),
            "effects": self.status_effects.copy(),
        }

    def get_history(self) -> List[Dict]:
        """Retourne l'historique des status"""
        return self.status_history

    def is_critical(self) -> bool:
        """Vérifie si l'agent est dans un état critique"""
        return any(stat < 20 for stat in self.stats.values())
