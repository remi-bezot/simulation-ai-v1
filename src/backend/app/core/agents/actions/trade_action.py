from app.core.agents.actions.base_agent_action import AgentAction
from app.application.interfaces.trade_action_interface import ITradeAction


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
        print(
            f"Initialisation de l'échange de ressources avec {self.target} par l'agent {agent}"
        )

    def execute(self, agent):
        """
        Fait échanger des ressources à l'agent avec un autre agent.

        :param agent: L'agent qui échange.
        """
        # Logique pour échanger des ressources
        print(
            f"L'agent {agent} échange des ressources avec {self.target} : {self.resources}"
        )

    def finalize(self, agent):
        """
        Finalise l'action d'échange pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        print(f"Finalisation de l'échange de l'agent {agent}")
