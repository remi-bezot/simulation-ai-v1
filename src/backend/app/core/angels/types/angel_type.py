from app.application.interfaces.angel_type_interface import IAngelType


class AngelType(IAngelType):
    """
    Classe de base pour les types d'anges.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'ange.

        :return: Le nom du type d'ange.
        """
        raise NotImplementedError("Subclasses should implement this method!")
