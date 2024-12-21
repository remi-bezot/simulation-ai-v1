from abc import ABC, abstractmethod


class IAgentBehavior(ABC):
    """
    Interface pour les comportements des agents.
    """

    @abstractmethod
    def perform(self, agent):
        """
        Exécute le comportement sur l'agent donné.

        :param agent: L'agent sur lequel le comportement est exécuté.
        """
        pass
