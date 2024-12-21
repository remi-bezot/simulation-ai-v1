from app.core.agents.actions.base_agent_action import AgentAction
from app.core.agents.actions.interfaces.i_trade_action import ITradeAction


class TradeAction(AgentAction, ITradeAction):
    """
    Action pour échanger des ressources avec un autre agent.
    """

    def __init__(self, target, resources: dict):
        self.target = target
        self.resources = resources

    def set_target(self, target):
        """
        Définit la cible de l'échange.

        :param target: La cible de l'échange.
        """
        self.target = target

    def set_resources(self, resources: dict):
        """
        Définit les ressources à échanger.

        :param resources: Les ressources à échanger.
        """
        self.resources = resources

    def initialize(self, agent):
        """
        Initialise l'action d'échange pour l'agent donné.

        :param agent: L'agent pour lequel l'action est initialisée.
        """
        # Implémentation de l'initialisation
        pass

    def execute(self, agent):
        """
        Exécute l'action d'échange sur l'agent donné.

        :param agent: L'agent sur lequel l'action est exécutée.
        """
        # Implémentation de l'exécution
        pass

    def finalize(self, agent):
        """
        Finalise l'action d'échange pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        # Implémentation de la finalisation
        pass
