from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)


class SimulationInterface(ABC):
    """
    Interface pour les simulations.
    """

    @abstractmethod
    def execute(self):
        """
        Exécute la simulation.
        """
        raise NotImplementedError("Subclasses should implement this!")


class SimulationRunner:
    """
    Classe pour exécuter une simulation.
    """

    def __init__(self, simulation: SimulationInterface):
        """
        Initialise le runner avec une simulation.

        :param simulation: Instance de SimulationInterface.
        """
        self.simulation = simulation

    def run(self):
        """
        Exécute la simulation et gère les exceptions.
        """
        try:
            logger.info("Début de l'exécution de la simulation.")
            self.simulation.execute()
            logger.info("Simulation exécutée avec succès.")
        except Exception as e:
            logger.error(f"Erreur lors de l'exécution de la simulation : {e}")
            raise RuntimeError(f"Erreur lors de l'exécution de la simulation : {e}")
