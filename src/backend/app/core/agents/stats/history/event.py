from dataclasses import dataclass
from datetime import datetime
from typing import Dict


@dataclass
class Event:
    """Classe représentant un événement"""

    timestamp: datetime
    value: float
    description: str

    def __post_init__(self):
        """Validation après initialisation"""
        if not isinstance(self.timestamp, datetime):
            raise TypeError("timestamp doit être un objet datetime")
        if not isinstance(self.value, (int, float)):
            raise TypeError("value doit être un nombre")
        if not isinstance(self.description, str):
            raise TypeError("description doit être une chaîne de caractères")

    def to_dict(self) -> Dict:
        """
        Convertit l'événement en dictionnaire.

        :return: Dictionnaire représentant l'événement
        """
        return {
            "timestamp": self.timestamp.isoformat(),
            "value": self.value,
            "description": self.description,
        }

    def __lt__(self, other):
        """Compare deux événements par leur timestamp"""
        return self.timestamp < other.timestamp

    def __str__(self):
        """Représentation lisible de l'événement"""
        return f"{self.timestamp.isoformat()} - {self.description}: {self.value}"
