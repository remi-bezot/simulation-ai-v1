from abc import ABC, abstractmethod


class IAngelType(ABC):
    """
    Interface pour les types d'anges.
    """

    @abstractmethod
    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'ange.

        :return: Le nom du type d'ange.
        """
        pass
