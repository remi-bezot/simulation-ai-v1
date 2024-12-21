from typing import Dict
from ...exceptions.metrics_exception import MetricsException
from ...interfaces.i_metrics_calculator import IMetricsCalculator


class MetricsCalculator(IMetricsCalculator):
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
                raise MetricsException(f"La métrique {key} doit être entre 0 et 100, reçu: {value}")
