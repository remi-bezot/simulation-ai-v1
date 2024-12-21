class EventException(Exception):
    """
    Exception de base pour les événements.
    """

    pass


class EventNotFoundException(EventException):
    """
    Exception levée lorsque l'événement n'est pas trouvé.
    """

    pass


class InvalidEventDataException(EventException):
    """
    Exception levée lorsque les données de l'événement sont invalides.
    """

    pass
