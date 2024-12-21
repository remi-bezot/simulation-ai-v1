from dataclasses import dataclass, field
from typing import Dict, List
from datetime import datetime


@dataclass
class Modifier:
    """Classe pour représenter un modificateur"""

    stat: str
    value: float
    duration: float = 0  # 0 = permanent
    start_time: datetime = field(default_factory=datetime.now)

    def is_expired(self) -> bool:
        if self.duration == 0:
            return False
        return (datetime.now() - self.start_time).total_seconds() > self.duration


@dataclass
class ModifiersHandler:
    """Gestionnaire des modificateurs de statistiques"""

    modifiers: List[Modifier] = field(default_factory=list)

    def add_modifier(self, stat: str, value: float, duration: float = 0) -> None:
        """
        Ajoute un nouveau modificateur.

        :param stat: Statistique à modifier
        :param value: Valeur du modificateur
        :param duration: Durée en secondes (0 = permanent)
        """
        self.modifiers.append(Modifier(stat, value, duration))

    def clean_expired_modifiers(self) -> None:
        """Nettoie les modificateurs expirés"""
        self.modifiers = [mod for mod in self.modifiers if not mod.is_expired()]

    def apply(self, stats: Dict) -> Dict:
        """
        Applique les modificateurs aux statistiques.

        :param stats: Dictionnaire des statistiques
        :return: Statistiques modifiées
        :raises KeyError: Si une statistique n'existe pas
        """
        try:
            self.clean_expired_modifiers()

            for modifier in self.modifiers:
                if "vitals" in stats and modifier.stat in stats["vitals"]:
                    current = stats["vitals"][modifier.stat]["current"]
                    stats["vitals"][modifier.stat]["current"] = min(
                        current * modifier.value,
                        stats["vitals"][modifier.stat]["maximum"],
                    )

            return stats

        except KeyError as e:
            raise KeyError(f"Statistique introuvable: {str(e)}")
        except Exception as e:
            raise ValueError(
                f"Erreur lors de l'application des modificateurs: {str(e)}"
            )
