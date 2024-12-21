from abc import ABC
from app.application.interfaces.agent_action_interface import IAgentAction


class IRestAction(IAgentAction, ABC):
    """
    Interface pour les actions de repos des agents.
    """

    pass
