from app.core.angels.types.angel_type import AngelType


class AngelJudges(AngelType):
    """
    Type d'ange pour les juges.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'ange.

        :return: Le nom du type d'ange.
        """
        return "Angel Judges"
