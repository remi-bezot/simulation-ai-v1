from app.core.ai.types.ai_type import AIType


class ChatbotAIType(AIType):
    """
    Type d'IA pour les chatbots.
    """

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'IA.

        :return: Le nom du type d'IA.
        """
        return "Chatbot"

    def respond_to_message(self, message: str) -> str:
        """
        Répond à un message.

        :param message: Le message reçu.
        :return: La réponse du chatbot.
        """
        # Implémentation de la réponse du chatbot
        return "Réponse du chatbot"
