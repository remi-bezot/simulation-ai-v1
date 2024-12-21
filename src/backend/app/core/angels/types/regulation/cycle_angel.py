from app.core.angels.types.angel_type import AngelType


class CycleAngel(AngelType):
    """
    Type d'ange pour les cycles.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'ange.

        :return: Le nom du type d'ange.
        """
        return "Cycle"
