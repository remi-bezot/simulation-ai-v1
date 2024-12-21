from app.application.interfaces.agent_type_interface import IAgentType


class AgentType(IAgentType):
    """
    Classe de base pour les types d'agents.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'agent.

        :return: Le nom du type d'agent.
        """
        raise NotImplementedError("Subclasses should implement this method!")
