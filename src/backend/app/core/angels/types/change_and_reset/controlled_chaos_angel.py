from app.core.angels.types.angel_type import AngelType


class ControlledChaosAngel(AngelType):
    """
    Type d'ange pour le chaos contrôlé.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'ange.

        :return: Le nom du type d'ange.
        """
        return "Controlled Chaos"
