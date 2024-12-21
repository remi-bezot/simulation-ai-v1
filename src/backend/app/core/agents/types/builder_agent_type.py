from app.core.agents.types.agent_type import AgentType


class BuilderAgentType(AgentType):
    """
    Type d'agent pour les constructeurs.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'agent.

        :return: Le nom du type d'agent.
        """
        return "Builder"
