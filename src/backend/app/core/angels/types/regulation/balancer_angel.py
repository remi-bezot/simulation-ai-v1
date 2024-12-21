from app.core.angels.types.angel_type import AngelType


class BalancerAngel(AngelType):
    """
    Type d'ange pour l'équilibre.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'ange.

        :return: Le nom du type d'ange.
        """
        return "Balancer"
