from app.core.angels.types.angel_type import AngelType


class CreativeChaosAngel(AngelType):
    """
    Type d'ange pour le chaos créatif.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'ange.

        :return: Le nom du type d'ange.
        """
        return "Creative Chaos"
