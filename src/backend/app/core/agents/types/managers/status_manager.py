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
        self.state_history: List[State] = []
        self.history_tracker = HistoryTracker()

    def update_status(self, delta_time: float):
        """
        Met à jour le statut de l'agent en fonction du temps écoulé.
        """
        self.stats["health"] -= delta_time * self.needs.get_health_decay()
        self.stats["morale"] -= delta_time * self.emotions.get_morale_decay()

        if self.stats["health"] <= 0:
            raise AgentDeadException("L'agent est mort.")

        # Enregistrer l'état actuel dans l'historique
        current_state = State(
            health=self.stats["health"],
            morale=self.stats["morale"],
            needs=self.needs.get_all_needs(),
            emotions=self.emotions.get_all_emotions(),
        )
        self.state_history.append(current_state)
        self.history_tracker.track_state(current_state)

    def get_status_effects(self) -> Dict[str, float]:
        """
        Retourne les effets de statut actuels de l'agent.
        """
        return self.status_effects

    def get_state_history(self) -> List[State]:
        """
        Retourne l'historique des états de l'agent.
        """
        return self.state_history

    def apply_status_effect(self, effect_name: str, effect_value: float):
        """
        Applique un effet de statut à l'agent.
        """
        self.status_effects[effect_name] = effect_value

    def remove_status_effect(self, effect_name: str):
        """
        Supprime un effet de statut de l'agent.
        """
        if effect_name in self.status_effects:
            del self.status_effects[effect_name]

    def get_tracked_history(self):
        """
        Retourne l'historique suivi par le HistoryTracker.
        """
        return self.history_tracker.get_history()

    def reset_status(self):
        """
        Réinitialise les statuts de l'agent.
        """
        self.status_effects.clear()
        self.stats["health"] = 100
        self.stats["morale"] = 100
        self.state_history.clear()
        self.history_tracker.reset()

    def update_needs(self, new_needs: Dict[str, float]):
        """
        Met à jour les besoins de l'agent.
        """
        self.needs.update_needs(new_needs)

    def update_emotions(self, new_emotions: Dict[str, float]):
        """
        Met à jour les émotions de l'agent.
        """
        self.emotions.update_emotions(new_emotions)

    def get_current_state(self) -> State:
        """
        Retourne l'état actuel de l'agent.
        """
        return State(
            health=self.stats["health"],
            morale=self.stats["morale"],
            needs=self.needs.get_all_needs(),
            emotions=self.emotions.get_all_emotions(),
        )

    def apply_combined_effects(self):
        """
        Applique les effets combinés des besoins et des émotions sur la santé et le moral.
        """
        combined_effect = (
            self.needs.get_combined_effect() + self.emotions.get_combined_effect()
        )
        self.stats["health"] += combined_effect
        self.stats["morale"] += combined_effect

    def get_needs_status(self) -> Dict[str, float]:
        """
        Retourne le statut actuel des besoins de l'agent.
        """
        return self.needs.get_all_needs()

    def get_emotions_status(self) -> Dict[str, float]:
        """
        Retourne le statut actuel des émotions de l'agent.
        """
        return self.emotions.get_all_emotions()

    def log_status(self):
        """
        Enregistre le statut actuel de l'agent dans le journal.
        """
        self.history_tracker.log_state(self.get_current_state())


# Ajoutez ici les autres méthodes et classes nécessaires
