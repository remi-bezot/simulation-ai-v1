from dataclasses import dataclass
from typing import Dict, Optional
from app.core.agents.stats.metrics.performance import PerformanceCalculator
from app.core.agents.stats.metrics.efficiency import EfficiencyCalculator
from app.core.agents.stats.metrics.durability import DurabilityCalculator
from ..exceptions.metrics_exception import MetricsException


@dataclass
class MetricsManager:
    """Gestionnaire des métriques d'un agent"""

    def get_metrics(self, stats: Dict) -> Dict[str, float]:
        """
        Retourne toutes les métriques calculées pour l'agent.

        :param stats: Dictionnaire contenant les statistiques de l'agent
        :return: Dictionnaire contenant toutes les métriques calculées
        :raises ValueError: Si les statistiques sont invalides
        """
        try:
            if not stats:
                raise ValueError("Les statistiques ne peuvent pas être vides")

            metrics = {}

            # Calcul des métriques de base
            metrics["performance"] = self._safe_calculate(
                PerformanceCalculator.calculate, stats
            )
            metrics["efficiency"] = self._safe_calculate(
                EfficiencyCalculator.calculate, stats
            )
            metrics["durability"] = self._safe_calculate(
                DurabilityCalculator.calculate, stats
            )

            # Calcul de la métrique composite
            metrics["overall_rating"] = self._calculate_overall_rating(metrics)

            return metrics

        except Exception as e:
            raise ValueError(f"Erreur lors du calcul des métriques: {str(e)}")

    def _safe_calculate(self, calculator_func, stats: Dict) -> float:
        """
        Calcule une métrique de manière sécurisée.

        :param calculator_func: Fonction de calcul à utiliser
        :param stats: Statistiques de l'agent
        :return: Valeur calculée ou 0 en cas d'erreur
        """
        try:
            return calculator_func(stats)
        except Exception:
            return 0.0

    def _calculate_overall_rating(self, metrics: Dict[str, float]) -> float:
        """
        Calcule la note globale basée sur toutes les métriques.

        :param metrics: Dictionnaire des métriques calculées
        :return: Note globale (entre 0 et 100)
        """
        weights = {"performance": 0.4, "efficiency": 0.3, "durability": 0.3}

        overall = sum(
            metrics[key] * weight for key, weight in weights.items() if key in metrics
        )

        return round(overall, 2)


class MetricsCalculator:
    """
    Classe pour calculer les métriques des agents.
    """

    def calculate_performance(self, data: Dict) -> float:
        """
        Calcule la performance basée sur les données fournies.

        :param data: Dictionnaire des données
        :return: Performance (entre 0 et 100)
        """
        # Implémentation du calcul de la performance
        pass

    def calculate_efficiency(self, data: Dict) -> float:
        """
        Calcule l'efficacité basée sur les données fournies.

        :param data: Dictionnaire des données
        :return: Efficacité (entre 0 et 100)
        """
        # Implémentation du calcul de l'efficacité
        pass

    def calculate_durability(self, data: Dict) -> float:
        """
        Calcule la durabilité basée sur les données fournies.

        :param data: Dictionnaire des données
        :return: Durabilité (entre 0 et 100)
        """
        # Implémentation du calcul de la durabilité
        pass

    def calculate_overall_score(self, metrics: Dict[str, float]) -> float:
        """
        Calcule la note globale basée sur toutes les métriques.

        :param metrics: Dictionnaire des métriques calculées
        :return: Note globale (entre 0 et 100)
        """
        weights = {"performance": 0.4, "efficiency": 0.3, "durability": 0.3}

        overall = sum(
            metrics[key] * weight for key, weight in weights.items() if key in metrics
        )

        return round(overall, 2)

    def validate_metrics(self, metrics: Dict[str, float]) -> None:
        """
        Valide les métriques fournies.

        :param metrics: Dictionnaire des métriques
        :raises MetricsException: Si les métriques sont invalides
        """
        for key, value in metrics.items():
            if not 0 <= value <= 100:
                raise MetricsException(
                    f"La métrique {key} doit être entre 0 et 100, reçu: {value}"
                )
