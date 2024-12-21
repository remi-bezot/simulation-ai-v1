from typing import List, Tuple, Any
from abc import ABC, abstractmethod


class IGeneticAlgorithm(ABC):
    """
    Interface pour les algorithmes génétiques.
    """

    @abstractmethod
    def initialize_population(self) -> List[Any]:
        """
        Initialise la population.

        :return: La population initiale.
        """
        pass

    @abstractmethod
    def create_individual(self) -> Any:
        """
        Crée un individu aléatoire.

        :return: Un individu.
        """
        pass

    @abstractmethod
    def select_parents(self) -> Tuple[Any, Any]:
        """
        Sélectionne les parents pour le croisement.

        :return: Un tuple contenant deux parents.
        """
        pass

    @abstractmethod
    def crossover(self, parent1: Any, parent2: Any) -> Any:
        """
        Effectue le croisement entre deux parents.

        :param parent1: Le premier parent.
        :param parent2: Le deuxième parent.
        :return: L'enfant résultant du croisement.
        """
        pass

    @abstractmethod
    def mutate(self, individual: Any) -> Any:
        """
        Effectue la mutation sur un individu.

        :param individual: L'individu à muter.
        :return: L'individu muté.
        """
        pass

    @abstractmethod
    def run(self, generations: int):
        """
        Exécute l'algorithme génétique.

        :param generations: Le nombre de générations à exécuter.
        """
        pass
