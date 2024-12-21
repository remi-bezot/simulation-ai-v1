from app.application.interfaces.agent_action_interface import IAgentAction


class IBuildAction(IAgentAction):
    """
    Interface pour les actions de construction des agents.
    """

    @abstractmethod
    def set_structure_type(self, structure_type: str):
        """
        Définit le type de structure à construire.

        :param structure_type: Le type de structure à construire.
        """
        pass
