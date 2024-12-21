from dataclasses import dataclass
from typing import Dict, Optional
from app.core.agents.types.interfaces.i_agent_type import IAgentType
from app.core.agents.exceptions.agent_exceptions import (
    AgentDeadException,
    InvalidValueException,
)
from app.core.agents.stats.calculators import StatsCalculator
from app.core.agents.stats.history import HistoryTracker
from app.core.agents.stats.metrics import MetricsManager
from app.core.agents.stats.modifiers import ModifiersHandler


@dataclass
class VitalStats:
    """
    Classe pour gérer les statistiques vitales d'un agent.
    """

    current: float
    maximum: float

    def modify(self, amount: float) -> float:
        """
        Modifie la valeur actuelle des statistiques vitales.

        :param amount: La quantité à ajouter ou soustraire
        :return: La nouvelle valeur des statistiques vitales
        """
        if amount < 0 and abs(amount) > self.current:
            raise InvalidValueException(
                "La valeur à soustraire est supérieure à la valeur actuelle."
            )
        new_value = max(0, min(self.maximum, self.current + amount))
        self.current = new_value
        return new_value


class BaseAgentType(IAgentType):
    """Classe de base pour tous les types d'agents"""

    def __init__(self, name: str):
        if not name:
            raise InvalidValueException("Le nom ne peut pas être vide")

        self.name = name
        self.health = VitalStats(100, 100)
        self.energy = VitalStats(100, 100)
        self.level = 1
        self.experience = 0
        self.alive = True
        self._validate_initial_state()
        self.stats_calculator = StatsCalculator()
        self.history_tracker = HistoryTracker()
        self.metrics_manager = MetricsManager()
        self.modifiers_handler = ModifiersHandler()

    def _validate_initial_state(self) -> None:
        """Valide l'état initial de l'agent"""
        if self.health.current <= 0:
            raise InvalidValueException("La santé initiale doit être positive")
        if self.energy.current <= 0:
            raise InvalidValueException("L'énergie initiale doit être positive")

    def get_name(self) -> str:
        """Retourne le nom de l'agent"""
        return self.name

    def is_alive(self) -> bool:
        """Vérifie si l'agent est en vie"""
        return self.alive and self.health.current > 0

    def modify_health(self, amount: float) -> Optional[float]:
        """
        Modifie les points de vie
        :raises AgentDeadException: Si l'agent est mort
        :return: Nouvelle valeur ou None si mort
        """
        if not self.is_alive():
            raise AgentDeadException("Impossible de modifier la santé d'un agent mort")

        new_health = self.health.modify(amount)
        if new_health <= 0:
            self.alive = False
            return None
        return new_health

    def modify_energy(self, amount: float) -> Optional[float]:
        """
        Modifie l'énergie
        :raises AgentDeadException: Si l'agent est mort
        :return: Nouvelle valeur ou None si échec
        """
        if not self.is_alive():
            raise AgentDeadException("Impossible de modifier l'énergie d'un agent mort")

        try:
            return self.energy.modify(amount)
        except InvalidValueException:
            return None

    def gain_experience(self, amount: float) -> None:
        """Gagne de l'expérience"""
        if self.is_alive():
            self.experience += amount
            self.check_level_up()

    def check_level_up(self) -> None:
        """Vérifie le niveau"""
        exp_needed = self.level * 100
        if self.experience >= exp_needed:
            self.level_up()

    def level_up(self) -> None:
        """Monte de niveau"""
        if self.is_alive():
            self.level += 1
            self.health.maximum += 10
            self.energy.maximum += 5
            self.health.current = self.health.maximum
            self.energy.current = self.energy.maximum

    def get_stats(self) -> Dict[str, any]:
        """Retourne les statistiques détaillées de l'agent"""
        base_stats = {
            "vitals": self._get_vital_stats(),
            "experience": self._get_experience_stats(),
            "status": self._get_status_stats(),
            "metrics": self.metrics_manager.get_metrics(),
            "history": self.history_tracker.get_history(),
        }

        return self.modifiers_handler.apply(base_stats)

    def _get_vital_stats(self) -> Dict[str, any]:
        """Retourne les statistiques vitales"""
        return {
            "health": self.stats_calculator.calculate_health_stats(self.health),
            "energy": self.stats_calculator.calculate_energy_stats(self.energy),
        }

    def _get_experience_stats(self) -> Dict[str, any]:
        """Retourne les statistiques d'expérience"""
        return self.stats_calculator.calculate_experience_stats(
            self.experience, self.level
        )

    def _get_status_stats(self) -> Dict[str, any]:
        """Retourne les statistiques de statut"""
        return {
            "alive": self.alive,
            "health_status": self.stats_calculator.get_health_status(self.health),
            "energy_status": self.stats_calculator.get_energy_status(self.energy),
        }
