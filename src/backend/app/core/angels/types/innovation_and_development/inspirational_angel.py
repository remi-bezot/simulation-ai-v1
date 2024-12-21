from app.core.angels.types.angel_type import AngelType


class InspirationalAngel(AngelType):
    """
    Type d'ange pour les inspirateurs.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'ange.

        :return: Le nom du type d'ange.
        """
        return "Inspirational Angel"
