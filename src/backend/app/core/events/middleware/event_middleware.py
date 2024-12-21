from app.core.events.interfaces.i_event import IEvent


class EventMiddleware:
    """
    Middleware pour le traitement des événements.
    """

    def process_event(self, event: IEvent):
        """
        Traite un événement avant qu'il ne soit géré.

        :param event: L'événement à traiter.
        """
        # Implémentation du traitement de l'événement
        pass
