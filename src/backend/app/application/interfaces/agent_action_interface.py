from abc import ABC, abstractmethod


class IAgentAction(ABC):
    """
    Interface pour les actions spécifiques aux agents.
    """

    @abstractmethod
    def initialize(self, agent):
        """
        Initialise l'action pour l'agent donné.

        :param agent: L'agent pour lequel l'action est initialisée.
        """
        pass

    @abstractmethod
    def execute(self, agent):
        """
        Exécute l'action sur l'agent donné.

        :param agent: L'agent sur lequel l'action est exécutée.
        """
        pass

    @abstractmethod
    def finalize(self, agent):
        """
        Finalise l'action pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        pass
