from typing import Dict
from app.core.agents.types.interfaces.i_agent_stats import IAgentStats


class AgentStats(IAgentStats):
    def __init__(self):
        self.health = 100
        self.energy = 100
        self.experience = 0
        self.level = 1
        self.max_health = 100
        self.max_energy = 100
        self.stats_limits = {
            "health": (0, self.max_health),
            "energy": (0, self.max_energy),
            "experience": (0, float("inf")),
        }

    def update_stat(self, stat: str, value: float) -> None:
        """
        Met à jour une statistique en respectant ses limites.

        :param stat: Le nom de la statistique à mettre à jour.
        :param value: La valeur à ajouter à la statistique.
        """
        if stat in self.__dict__:
            current = getattr(self, stat)
            if stat in self.stats_limits:
                min_val, max_val = self.stats_limits[stat]
                new_value = max(min_val, min(max_val, current + value))
                setattr(self, stat, new_value)

    def get_stats(self) -> Dict[str, float]:
        """Retourne toutes les statistiques"""
        return {
            "health": self.health,
            "energy": self.energy,
            "experience": self.experience,
            "level": self.level,
        }

    def gain_experience(self, amount: float) -> None:
        """Gagne de l'expérience et monte de niveau si nécessaire"""
        self.experience += amount
        self.check_level_up()

    def check_level_up(self) -> None:
        """Vérifie et applique la montée de niveau"""
        exp_needed = self.level * 100
        if self.experience >= exp_needed:
            self.level_up()

    def level_up(self) -> None:
        """Monte de niveau et augmente les stats max"""
        self.level += 1
        self.max_health += 10
        self.max_energy += 5
        self.health = self.max_health
        self.energy = self.max_energy
        self.stats_limits["health"] = (0, self.max_health)
        self.stats_limits["energy"] = (0, self.max_energy)
