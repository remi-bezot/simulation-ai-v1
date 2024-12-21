from app.core.angels.types.angel_type import AngelType


class EvolutionAngel(AngelType):
    """
    Type d'ange pour l'évolution.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'ange.

        :return: Le nom du type d'ange.
        """
        return "Evolution"
