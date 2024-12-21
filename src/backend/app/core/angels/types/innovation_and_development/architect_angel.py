from app.core.angels.types.angel_type import AngelType


class ArchitectAngel(AngelType):
    """
    Type d'ange pour les architectes.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'ange.

        :return: Le nom du type d'ange.
        """
        return "Architect"
