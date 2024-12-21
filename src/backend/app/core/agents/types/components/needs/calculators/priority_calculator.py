from dataclasses import dataclass, field
from typing import Dict, Optional, List
from app.core.agents.types.components.needs.interfaces.i_priority_calculator import (
    IPriorityCalculator,
)
from app.core.agents.types.components.needs.strategies.priority_strategies import (
    BasePriorityStrategy,
)


@dataclass
class PriorityCalculator(IPriorityCalculator):
    """Calculateur de priorités avec cache et stratégies multiples"""

    strategy: BasePriorityStrategy
    _cache: Dict[str, int] = field(default_factory=dict)
    _cache_size: int = field(default=100)
    _cache_hits: int = field(default=0)
    _cache_misses: int = field(default=0)
    _priority_history: List[Dict[str, int]] = field(default_factory=list)

    def calculate(
        self,
        need: str,
        base_priority: int,
        urgency: float,
        current_value: Optional[float] = None,
    ) -> int:
        """
        Calcule la priorité d'un besoin.

        :param need: Le besoin à évaluer
        :param base_priority: Priorité de base
        :param urgency: Urgence du besoin
        :param current_value: Valeur actuelle du besoin, peut être None
        :return: La priorité calculée
        """
        if current_value is None:
            current_value = 0.0  # Valeur par défaut si current_value est None

        # Ajoutez ici la logique de calcul de priorité en utilisant la stratégie
        priority = self.strategy.calculate_priority(
            base_priority, urgency, current_value
        )

        # Gestion du cache
        if need in self._cache:
            self._cache_hits += 1
        else:
            self._cache_misses += 1
            if len(self._cache) >= self._cache_size:
                self._cache.pop(next(iter(self._cache)))
            self._cache[need] = priority

        # Enregistrer l'historique des priorités
        self._priority_history.append({need: priority})

        return priority

    def get_priority_history(self) -> List[Dict[str, int]]:
        """
        Retourne l'historique des priorités calculées.

        :return: Liste de dictionnaires contenant les priorités calculées
        """
        return self._priority_history


# Ajoutez ici les autres méthodes et classes nécessaires
