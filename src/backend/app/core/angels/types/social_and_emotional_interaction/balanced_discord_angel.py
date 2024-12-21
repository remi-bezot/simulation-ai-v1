from app.core.angels.types.angel_type import AngelType


class BalancedDiscordAngel(AngelType):
    """
    Type d'ange pour la discorde équilibrée.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'ange.

        :return: Le nom du type d'ange.
        """
        return "Balanced Discord"
