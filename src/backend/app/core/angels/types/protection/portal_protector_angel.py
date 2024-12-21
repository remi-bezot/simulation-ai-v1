from app.core.angels.types.angel_type import AngelType


class PortalProtectorAngel(AngelType):
    """
    Type d'ange pour les protecteurs des portails.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'ange.

        :return: Le nom du type d'ange.
        """
        return "Portal Protector"
