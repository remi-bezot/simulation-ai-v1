from typing import Dict


class DurabilityCalculator:
    """Classe pour calculer la durabilité globale d'un agent"""

    @staticmethod
    def calculate(stats: Dict) -> float:
        """
        Calcule la durabilité basée sur la santé et d'autres facteurs.

        :param stats: Dictionnaire contenant les statistiques de l'agent
        :return: La durabilité calculée (entre 0 et 100)
        :raises KeyError: Si les statistiques requises sont manquantes
        :raises ValueError: Si les valeurs ne sont pas dans la plage valide
        """
        try:
            health = stats["vitals"]["health"]["percentage"]
            resistance = stats.get("resistance", {}).get("value", 1.0)
            armor = stats.get("armor", {}).get("value", 1.0)

            if not all(
                isinstance(x, (int, float)) for x in [health, resistance, armor]
            ):
                raise ValueError("Les valeurs doivent être numériques")

            if not 0 <= health <= 100:
                raise ValueError("La santé doit être entre 0 et 100")

            durability = (health * resistance * armor) / (resistance + armor)
            return round(durability, 2)

        except KeyError:
            raise KeyError("Statistiques de durabilité manquantes")
