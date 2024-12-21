# Algorithmes génétiques

import random
from typing import List, Tuple, Any
from app.core.genetics.interfaces.i_genetic_algorithm import IGeneticAlgorithm


class GeneticAlgorithm(IGeneticAlgorithm):
    """
    Classe de base pour les algorithmes génétiques.
    """

    def __init__(
        self, population_size: int, mutation_rate: float, crossover_rate: float
    ):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.population = self.initialize_population()

    def initialize_population(self) -> List[Any]:
        """
        Initialise la population.

        :return: La population initiale.
        """
        # Exemple d'initialisation de la population avec des individus aléatoires
        return [self.create_individual() for _ in range(self.population_size)]

    def create_individual(self) -> Any:
        """
        Crée un individu aléatoire.

        :return: Un individu.
        """
        # Implémentation de la création d'un individu
        return random.random()

    def select_parents(self) -> Tuple[Any, Any]:
        """
        Sélectionne les parents pour le croisement.

        :return: Un tuple contenant deux parents.
        """
        # Sélection aléatoire de deux parents
        parent1 = random.choice(self.population)
        parent2 = random.choice(self.population)
        return parent1, parent2

    def crossover(self, parent1: Any, parent2: Any) -> Any:
        """
        Effectue le croisement entre deux parents.

        :param parent1: Le premier parent.
        :param parent2: Le deuxième parent.
        :return: L'enfant résultant du croisement.
        """
        # Exemple de croisement simple
        return (parent1 + parent2) / 2

    def mutate(self, individual: Any) -> Any:
        """
        Effectue la mutation sur un individu.

        :param individual: L'individu à muter.
        :return: L'individu muté.
        """
        # Exemple de mutation simple
        if random.random() < self.mutation_rate:
            individual += random.uniform(-0.1, 0.1)
        return individual

    def run(self, generations: int):
        """
        Exécute l'algorithme génétique.

        :param generations: Le nombre de générations à exécuter.
        """
        for generation in range(generations):
            new_population = []
            for _ in range(self.population_size // 2):
                parent1, parent2 = self.select_parents()
                child1 = self.crossover(parent1, parent2)
                child2 = self.crossover(parent2, parent1)
                new_population.append(self.mutate(child1))
                new_population.append(self.mutate(child2))
            self.population = new_population
