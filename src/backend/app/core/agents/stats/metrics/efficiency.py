from typing import Dict


class EfficiencyCalculator:
    """Classe pour calculer l'efficacité globale d'un agent"""

    @staticmethod
    def calculate(stats: Dict) -> float:
        """
        Calcule l'efficacité globale basée sur les statistiques.

        :param stats: Dictionnaire contenant les statistiques de l'agent
        :return: L'efficacité calculée (entre 0 et 100)
        :raises KeyError: Si les statistiques requises sont manquantes
        :raises ValueError: Si les valeurs ne sont pas dans la plage valide
        """
        try:
            efficiency = stats["experience"]["efficiency"]
            if not isinstance(efficiency, (int, float)):
                raise ValueError("L'efficacité doit être un nombre")
            if efficiency < 0 or efficiency > 100:
                raise ValueError("L'efficacité doit être entre 0 et 100")
            return round(efficiency, 2)
        except KeyError:
            raise KeyError("Statistiques d'efficacité manquantes")
