from app.core.angels.types.interfaces.i_angel_type import IAngelType


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
