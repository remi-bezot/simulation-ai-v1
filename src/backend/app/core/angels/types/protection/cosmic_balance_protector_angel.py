from app.core.angels.types.angel_type import AngelType


class CosmicBalanceProtectorAngel(AngelType):
    """
    Type d'ange pour les protecteurs de l'équilibre cosmique.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'ange.

        :return: Le nom du type d'ange.
        """
        return "Cosmic Balance Protector"
