from app.core.angels.types.angel_type import AngelType


class AngelOfJustice(AngelType):
    """
    Type d'ange pour la justice.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'ange.

        :return: Le nom du type d'ange.
        """
        return "Angel of Justice"
