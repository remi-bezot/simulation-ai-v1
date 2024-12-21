from typing import Dict
from app.core.agents.types.components.health import Health
from app.core.agents.types.components.energy import Energy
from app.core.agents.types.components.experience import Experience


class AgentBase:
    def __init__(self, name: str):
        self.name = name
        self.health = Health(100, 100)
        self.energy = Energy(100, 100)
        self.experience = Experience()

    def get_stats(self) -> Dict[str, float]:
        """Retourne les statistiques de base"""
        return {
            "name": self.name,
            "health": self.health.current,
            "max_health": self.health.maximum,
            "energy": self.energy.current,
            "max_energy": self.energy.maximum,
            "experience": self.experience.current,
            "level": self.experience.level,
        }

    def modify_health(self, amount: float) -> None:
        """Modifie les points de vie"""
        self.health.modify(amount)

    def modify_energy(self, amount: float) -> bool:
        """Modifie l'énergie"""
        return self.energy.modify(amount)

    def gain_experience(self, amount: float) -> None:
        """Gagne de l'expérience"""
        self.experience.gain(amount)

    def is_alive(self) -> bool:
        """Vérifie si l'agent est en vie"""
        return self.health.is_alive()
