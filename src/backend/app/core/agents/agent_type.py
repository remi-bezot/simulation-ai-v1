from app.core.agents.types.interfaces.i_agent_type import IAgentType
from app.core.components.emotions import Emotions
from app.core.components.needs import Needs
from app.core.components.skills import Skills
from app.core.components.resources import Resources
from app.core.components.state import State


class AgentType(IAgentType):
    """
    Classe de base pour les types d'agents.
    """

    def __init__(self, name: str):
        self.name = name
        self.emotions = Emotions()
        self.needs = Needs()
        self.skills = Skills()
        self.resources = Resources()
        self.state = State()
        self.aspiration = None
        self.health = 100

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'agent.

        :return: Le nom du type d'agent.
        """
        raise NotImplementedError("Subclasses should implement this method!")

    def set_aspiration(self, aspiration: str):
        """
        Définir une aspiration.

        :param aspiration: L'aspiration à définir.
        """
        self.aspiration = aspiration

    def has_aspiration(self) -> bool:
        """
        Vérifier si une aspiration est définie.

        :return: True si une aspiration est définie, sinon False.
        """
        return self.aspiration is not None

    def interact_with(self, other_agent, interaction_type: str):
        """
        Interagir avec un autre agent.

        :param other_agent: L'autre agent avec lequel interagir.
        :param interaction_type: Le type d'interaction.
        """
        # Implémentation de l'interaction
        pass

    def make_decision(self):
        """
        Prendre une décision basée sur les objectifs et les priorités.
        """
        # Implémentation de la prise de décision
        pass

    def react_to_environment(self, change: str):
        """
        Réagir aux changements dans l'environnement.

        :param change: Le changement dans l'environnement.
        """
        # Implémentation de la réaction
        pass

    def manage_health(self, change: float):
        """
        Gérer la santé de l'agent.

        :param change: Le changement de la santé.
        """
        self.health += change
        if self.health > 100:
            self.health = 100
        elif self.health < 0:
            self.health = 0

    def update(self):
        """
        Mettre à jour l'état de l'agent.
        """
        # Implémentation de la mise à jour de l'état
        pass
