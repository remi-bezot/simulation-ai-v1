from typing import Dict


class PerformanceCalculator:
    """Classe pour calculer la performance globale"""

    @staticmethod
    def calculate(stats: Dict) -> float:
        """
        Calcule la performance globale.

        :param stats: Un dictionnaire contenant les statistiques de l'agent.
        :return: La performance globale calculée.
        :raises KeyError: Si une clé nécessaire est manquante dans le dictionnaire.
        """
        try:
            health = stats["vitals"]["health"]["percentage"]
            energy = stats["vitals"]["energy"]["percentage"]
            experience = stats["experience"]["percentage"]
        except KeyError as e:
            raise KeyError(f"Clé manquante dans les statistiques: {e}")

        return round((health + energy + experience) / 3, 2)
