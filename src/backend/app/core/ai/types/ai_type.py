from app.application.interfaces.ai_type_interface import IAIType


class AIType(IAIType):
    """
    Classe de base pour les types d'IA.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'IA.

        :return: Le nom du type d'IA.
        """
        raise NotImplementedError("Subclasses should implement this method!")
