from dataclasses import dataclass, field
from typing import Dict, List, Optional
from datetime import datetime


@dataclass
class HistoryTracker:
    """Classe pour suivre l'historique des événements"""

    history: Dict[str, List[Dict[str, any]]] = field(default_factory=dict)

    def add_event(self, category: str, value: float, description: str) -> None:
        """
        Ajoute un événement à l'historique.

        :param category: La catégorie de l'événement
        :param value: La valeur associée à l'événement
        :param description: La description de l'événement
        """
        if category not in self.history:
            self.history[category] = []

        self.history[category].append(
            {"timestamp": datetime.now(), "value": value, "description": description}
        )

    def get_history(
        self, category: Optional[str] = None
    ) -> Dict[str, List[Dict[str, any]]]:
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
