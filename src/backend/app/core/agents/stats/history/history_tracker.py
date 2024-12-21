from typing import Dict, List, Optional
from app.core.agents.stats.history.event import Event
from datetime import datetime


class HistoryTracker:
    """Classe pour suivre l'historique des événements"""

    def __init__(self):
        self.history: Dict[str, List[Event]] = {}

    def add_event(self, category: str, value: float, description: str) -> None:
        """
        Ajoute un événement à l'historique.

        :param category: La catégorie de l'événement
        :param value: La valeur associée à l'événement
        :param description: La description de l'événement
        :raises ValueError: Si la catégorie, la valeur ou la description sont invalides
        """
        if not category or not isinstance(category, str):
            raise ValueError(
                "La catégorie doit être une chaîne de caractères non vide."
            )
        if not isinstance(value, (int, float)):
            raise ValueError("La valeur doit être un nombre.")
        if not description or not isinstance(description, str):
            raise ValueError(
                "La description doit être une chaîne de caractères non vide."
            )

        if category not in self.history:
            self.history[category] = []

        self.history[category].append(
            Event(timestamp=datetime.now(), value=value, description=description)
        )

    def get_history(self, category: Optional[str] = None) -> Dict[str, List[Event]]:
        """
        Retourne l'historique des événements.

        :param category: La catégorie spécifique à retourner (optionnel)
        :return: Un dictionnaire contenant l'historique
        """
        if category:
            return {category: self.history.get(category, [])}
        return self.history

    def clear_history(self, category: Optional[str] = None) -> None:
        """
        Efface l'historique des événements.

        :param category: La catégorie spécifique à effacer (optionnel)
        """
        if category:
            if category in self.history:
                del self.history[category]
        else:
            self.history.clear()
