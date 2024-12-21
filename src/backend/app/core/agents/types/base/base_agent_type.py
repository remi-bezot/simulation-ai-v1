from app.core.agents.types.interfaces.i_agent_type import IAgentType


class BaseAgentType(IAgentType):
    """Classe de base pour tous les types d'agents"""

    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.energy = 100
        self.max_health = 100
        self.max_energy = 100
        self.alive = True
        self.level = 1

    def get_name(self) -> str:
        """Retourne le nom de l'agent"""
        return self.name

    def is_alive(self) -> bool:
        """Vérifie si l'agent est en vie"""
        return self.alive and self.health > 0

    def heal(self, amount: float):
        """Soigne l'agent"""
        if self.is_alive():
            self.health = min(self.max_health, self.health + amount)

    def take_damage(self, amount: float):
        """Inflige des dégâts à l'agent"""
        if self.is_alive():
            self.health = max(0, self.health - amount)
            if self.health <= 0:
                self.alive = False

    def restore_energy(self, amount: float):
        """Restaure l'énergie de l'agent"""
        if self.is_alive():
            self.energy = min(self.max_energy, self.energy + amount)

    def use_energy(self, amount: float) -> bool:
        """Utilise de l'énergie si disponible"""
        if self.is_alive() and self.energy >= amount:
            self.energy -= amount
            return True
        return False

    def level_up(self):
        """Augmente le niveau de l'agent"""
        if self.is_alive():
            self.level += 1
            self.max_health += 10
            self.max_energy += 5
            self.health = self.max_health
            self.energy = self.max_energy

    def get_stats(self) -> dict:
        """Retourne les statistiques de base de l'agent"""
        return {
            "name": self.name,
            "health": self.health,
            "max_health": self.max_health,
            "energy": self.energy,
            "max_energy": self.max_energy,
            "level": self.level,
            "alive": self.alive,
        }
