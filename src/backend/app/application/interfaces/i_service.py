from abc import ABC, abstractmethod


class IService(ABC):
    """
    Interface pour les services généraux.
    """

    @abstractmethod
    def execute(self):
        """
        Exécute le service.
        """
        pass
