from dataclasses import dataclass
from typing import Dict, Optional
from app.core.agents.types.base.base_agent_type import VitalStats


@dataclass
class StatsCalculator:
    """Calcule les différentes statistiques d'un agent"""

    def calculate_health_stats(self, health: VitalStats) -> Dict[str, any]:
        """
        Calcule les statistiques de santé.

        :param health: Les statistiques vitales de santé.
        :return: Un dictionnaire contenant les statistiques de santé.
        """
        return {
            "current": health.current,
            "maximum": health.maximum,
            "percentage": self._calculate_percentage(health),
            "status": self._get_health_status(health),
            "regeneration_rate": self._calculate_regen_rate(health),
        }

    def calculate_energy_stats(self, energy: VitalStats) -> Dict[str, any]:
        """
        Calcule les statistiques d'énergie.

        :param energy: Les statistiques vitales d'énergie.
        :return: Un dictionnaire contenant les statistiques d'énergie.
        """
        return {
            "current": energy.current,
            "maximum": energy.maximum,
            "percentage": self._calculate_percentage(energy),
            "status": self._get_energy_status(energy),
            "regeneration_rate": self._calculate_regen_rate(energy),
        }

    def calculate_experience_stats(
        self, experience: float, level: int
    ) -> Dict[str, any]:
        """Calcule les statistiques d'expérience"""
        next_level_exp = self._calculate_next_level_exp(level)
        return {
            "current": experience,
            "next_level": next_level_exp,
            "total_needed": next_level_exp,
            "percentage": self._calculate_level_progress(experience, next_level_exp),
            "efficiency": self._calculate_exp_efficiency(level, experience),
        }

    def _calculate_percentage(self, stats: VitalStats) -> float:
        """
        Calcule le pourcentage actuel.

        :param stats: Les statistiques vitales.
        :return: Le pourcentage actuel.
        """
        return (stats.current / stats.maximum) * 100

    def _get_health_status(self, health: VitalStats) -> str:
        """
        Détermine le statut de santé.

        :param health: Les statistiques vitales de santé.
        :return: Le statut de santé.
        """
        if health.current == health.maximum:
            return "Healthy"
        elif health.current > health.maximum * 0.5:
            return "Injured"
        else:
            return "Critical"

    def _get_energy_status(self, energy: VitalStats) -> str:
        """
        Détermine le statut d'énergie.

        :param energy: Les statistiques vitales d'énergie.
        :return: Le statut d'énergie.
        """
        if energy.current == energy.maximum:
            return "Energetic"
        elif energy.current > energy.maximum * 0.5:
            return "Tired"
        else:
            return "Exhausted"

    def _calculate_regen_rate(self, stats: VitalStats) -> float:
        """
        Calcule le taux de régénération.

        :param stats: Les statistiques vitales.
        :return: Le taux de régénération.
        """
        return stats.maximum * 0.01

    def _calculate_consumption_rate(self, energy: VitalStats) -> float:
        """Calcule le taux de consommation d'énergie"""
        base_rate = 0.05
        return base_rate * (energy.maximum / 100)

    def _calculate_next_level_exp(self, level: int) -> float:
        """Calcule l'expérience nécessaire pour le prochain niveau"""
        return level * 100

    def _calculate_level_progress(self, experience: float, next_level: float) -> float:
        """Calcule le pourcentage de progression vers le prochain niveau"""
        return round((experience / next_level) * 100, 2)

    def _calculate_exp_efficiency(self, level: int, experience: float) -> float:
        """Calcule l'efficacité de l'expérience"""
        expected_exp = level * 75
        return round((experience / expected_exp) * 100, 2)
