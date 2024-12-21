from dataclasses import dataclass, field
from typing import Dict, List
from statistics import mean


@dataclass
class NeedStats:
    """Statistiques détaillées des besoins"""

    satisfaction_rates: Dict[str, List[float]] = field(default_factory=dict)
    decay_rates: Dict[str, List[float]] = field(default_factory=dict)
    recovery_rates: Dict[str, List[float]] = field(default_factory=dict)

    def update_stats(
        self, need: str, value: float, decay: float, recovery: float
    ) -> None:
        if need not in self.satisfaction_rates:
            self.satisfaction_rates[need] = []
            self.decay_rates[need] = []
            self.recovery_rates[need] = []

        self.satisfaction_rates[need].append(value)
        self.decay_rates[need].append(decay)
        self.recovery_rates[need].append(recovery)

    def get_average_satisfaction(self, need: str) -> float:
        """Calcule la satisfaction moyenne pour un besoin"""
        return mean(self.satisfaction_rates.get(need, [0]))

    def get_average_decay(self, need: str) -> float:
        """Calcule le taux de décroissance moyen"""
        return mean(self.decay_rates.get(need, [0]))

    def get_average_recovery(self, need: str) -> float:
        """Calcule le taux de récupération moyen"""
        return mean(self.recovery_rates.get(need, [0]))

    def get_need_trend(self, need: str, window: int = 10) -> float:
        """
        Calcule la tendance d'un besoin sur une fenêtre donnée.

        :param need: Le besoin à analyser
        :param window: Taille de la fenêtre d'analyse
        :return: Tendance (-1 à 1)
        """
        values = self.satisfaction_rates.get(need, [])
        if len(values) < window:
            return 0.0

        recent = values[-window:]
        return (recent[-1] - recent[0]) / window

    def get_need_volatility(self, need: str) -> float:
        """
        Calcule la volatilité d'un besoin.

        :param need: Le besoin à analyser
        :return: Indice de volatilité
        """
        values = self.satisfaction_rates.get(need, [])
        if not values:
            return 0.0

        avg = mean(values)
        variance = mean((x - avg) ** 2 for x in values)
        return (variance**0.5) / avg if avg > 0 else 0.0

    def get_need_summary(self, need: str) -> Dict:
        """
        Retourne un résumé des statistiques pour un besoin.

        :param need: Le besoin à analyser
        :return: Dictionnaire des statistiques
        """
        return {
            "satisfaction": {
                "current": (
                    self.satisfaction_rates.get(need, [])[-1]
                    if self.satisfaction_rates.get(need)
                    else 0
                ),
                "average": self.get_average_satisfaction(need),
                "trend": self.get_need_trend(need),
                "volatility": self.get_need_volatility(need),
            },
            "decay": {
                "average": self.get_average_decay(need),
                "current": (
                    self.decay_rates.get(need, [])[-1]
                    if self.decay_rates.get(need)
                    else 0
                ),
            },
            "recovery": {
                "average": self.get_average_recovery(need),
                "current": (
                    self.recovery_rates.get(need, [])[-1]
                    if self.recovery_rates.get(need)
                    else 0
                ),
            },
        }

    def reset_stats(self, need: str) -> None:
        """Réinitialise les statistiques d'un besoin"""
        if need in self.satisfaction_rates:
            self.satisfaction_rates[need] = []
            self.decay_rates[need] = []
            self.recovery_rates[need] = []

    def trim_history(self, max_size: int = 1000) -> None:
        """
        Limite la taille de l'historique.

        :param max_size: Taille maximale de l'historique
        """
        for need in self.satisfaction_rates:
            self.satisfaction_rates[need] = self.satisfaction_rates[need][-max_size:]
            self.decay_rates[need] = self.decay_rates[need][-max_size:]
            self.recovery_rates[need] = self.recovery_rates[need][-max_size:]
