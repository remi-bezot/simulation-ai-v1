from abc import ABC, abstractmethod


class IAgentAction(ABC):
    @abstractmethod
    def initialize(self, agent) -> None:
        """
        Initialise l'action pour l'agent donné.

        :param agent: L'agent pour lequel l'action est initialisée.
        """
        pass

    @abstractmethod
    def execute(self, agent) -> None:
        """
        Exécute l'action sur l'agent donné.

        :param agent: L'agent sur lequel l'action est exécutée.
        """
        raise NotImplementedError("Subclasses should implement this method!")

    @abstractmethod
    def finalize(self, agent) -> None:
        """
        Finalise l'action pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        pass
