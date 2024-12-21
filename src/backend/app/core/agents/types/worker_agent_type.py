from app.core.agents.types.agent_type import AgentType


class WorkerAgentType(AgentType):
    """
    Type d'agent pour les travailleurs.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'agent.

        :return: Le nom du type d'agent.
        """
        return "Worker"
