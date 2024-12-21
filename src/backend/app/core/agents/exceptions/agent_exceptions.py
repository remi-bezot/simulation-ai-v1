class AgentException(Exception):
    """Exception de base pour les agents"""

    pass


class AgentDeadException(AgentException):
    """Exception levée quand une action est tentée sur un agent mort"""

    pass


class InvalidValueException(AgentException):
    """Exception levée quand une valeur invalide est utilisée"""

    pass


class InsufficientResourceException(AgentException):
    """Exception levée quand il manque des ressources"""

    pass


class InvalidActionException(AgentException):
    """Exception levée quand une action est invalide"""

    pass
