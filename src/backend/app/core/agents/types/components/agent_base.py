from typing import Dict


class AgentBase:
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.energy = 100
        self.experience = 0
        self.level = 1
        self.max_health = 100
        self.max_energy = 100

    def get_stats(self) -> Dict[str, float]:
        """Retourne les statistiques de base"""
        return {
            "name": self.name,
            "health": self.health,
            "energy": self.energy,
            "experience": self.experience,
            "level": self.level,
        }

    def modify_health(self, amount: float) -> None:
        """Modifie les points de vie"""
        self.health = max(0, min(self.max_health, self.health + amount))

    def modify_energy(self, amount: float) -> None:
        """Modifie l'énergie"""
        self.energy = max(0, min(self.max_energy, self.energy + amount))

    def gain_experience(self, amount: float) -> None:
        """Gagne de l'expérience"""
        self.experience += amount
        self.check_level_up()

    def check_level_up(self) -> None:
        """Vérifie la montée de niveau"""
        exp_needed = self.level * 100
        if self.experience >= exp_needed:
            self.level_up()

    def level_up(self) -> None:
        """Monte de niveau"""
        self.level += 1
        self.max_health += 10
        self.max_energy += 5
        self.health = self.max_health
        self.energy = self.max_energy

    def is_alive(self) -> bool:
        """Vérifie si l'agent est en vie"""
        return self.health > 0
