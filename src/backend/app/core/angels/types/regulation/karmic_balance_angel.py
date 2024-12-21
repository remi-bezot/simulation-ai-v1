from app.core.angels.types.angel_type import AngelType


class KarmicBalanceAngel(AngelType):
    """
    Type d'ange pour la balance karmique.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'ange.

        :return: Le nom du type d'ange.
        """
        return "Karmic Balance"
