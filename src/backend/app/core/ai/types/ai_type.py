from app.application.interfaces.ai_type_interface import IAIType


class AIType(IAIType):
    """
    Classe de base pour les types d'IA.
    """

    def __init__(self, name: str):
        self.name = name
        self.emotions = {}
        self.needs = {}
        self.aspiration = None
        self.skills = []

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'IA.

        :return: Le nom du type d'IA.
        """
        raise NotImplementedError("Subclasses should implement this method!")

    def feel_emotion(self, emotion: str, intensity: float):
        """
        Ressentir une émotion.
        """
        self.emotions[emotion] = intensity

    def perceive_environment(self, perception: str):
        """
        Percevoir l'environnement.
        """
        # Implémentation de la perception
        pass

    def satisfy_need(self, need: str, amount: float):
        """
        Satisfaire un besoin.
        """
        if need in self.needs:
            self.needs[need] -= amount

    def set_aspiration(self, aspiration: str):
        """
        Définir une aspiration.
        """
        self.aspiration = aspiration

    def learn_skill(self, skill: str):
        """
        Apprendre une nouvelle compétence.
        """
        self.skills.append(skill)

    def update(self):
        """
        Mettre à jour l'état de l'IA.
        """
        # Implémentation de la mise à jour de l'état
        pass
