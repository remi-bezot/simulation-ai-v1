from abc import ABC, abstractmethod


class IAgentType(ABC):
    """
    Interface pour les types d'agents.
    """

    @abstractmethod
    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'agent.

        :return: Le nom du type d'agent.
        """
        pass
