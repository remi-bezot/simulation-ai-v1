from app.core.angels.types.angel_type import AngelType


class CollectiveJudgmentAngel(AngelType):
    """
    Type d'ange pour le jugement collectif.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'ange.

        :return: Le nom du type d'ange.
        """
        return "Collective Judgment"
