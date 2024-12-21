from abc import ABC, abstractmethod


class IAIType(ABC):
    """
    Interface pour les types d'IA.
    """

    @abstractmethod
    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'IA.

        :return: Le nom du type d'IA.
        """
        pass
