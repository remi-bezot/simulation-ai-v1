from dataclasses import dataclass, field
from typing import Dict, Optional, List
from ..interfaces.i_priority_calculator import IPriorityCalculator
from ..strategies.priority_strategies import BasePriorityStrategy


@dataclass
class PriorityCalculator(IPriorityCalculator):
    """Calculateur de priorités avec cache et stratégies multiples"""

    strategy: BasePriorityStrategy
    _cache: Dict[str, int] = field(default_factory=dict)
    _cache_size: int = field(default=100)
    _cache_hits: int = field(default=0)
    _cache_misses: int = field(default=0)

    def calculate(
        self, need: str, base_priority: int, urgency: float, current_value: float
    ) -> int:
        """
        Calcule la priorité d'un besoin.

        :param need: Le besoin à évaluer
        :param base_priority: Priorité de base
        :param urgency: Facteur d'urgence
        :param current_value: Valeur actuelle
        :return: Score de priorité calculé
        """
        cache_key = f"{need}:{base_priority}:{urgency}:{current_value}"

        if cache_key in self._cache:
            self._cache_hits += 1
            return self._cache[cache_key]

        self._cache_misses += 1
        priority = self._calculate_priority(base_priority, urgency, current_value)

        self._update_cache(cache_key, priority)
        return priority

    def _calculate_priority(
        self, base_priority: int, urgency: float, current_value: float
    ) -> int:
        """Calcul effectif de la priorité"""
        if not self._validate_inputs(base_priority, urgency, current_value):
            raise ValueError("Valeurs d'entrée invalides")

        return self.strategy.calculate_priority(base_priority, urgency, current_value)

    def _validate_inputs(
        self, base_priority: int, urgency: float, current_value: float
    ) -> bool:
        """Valide les entrées"""
        return (
            isinstance(base_priority, int)
            and 0 <= urgency <= 1
            and 0 <= current_value <= 100
        )

    def _update_cache(self, key: str, value: int) -> None:
        """Met à jour le cache avec gestion de la taille"""
        if len(self._cache) >= self._cache_size:
            # Supprime la première entrée si le cache est plein
            self._cache.pop(next(iter(self._cache)))
        self._cache[key] = value

    def get_cache_stats(self) -> Dict[str, int]:
        """Retourne les statistiques du cache"""
        return {
            "hits": self._cache_hits,
            "misses": self._cache_misses,
            "size": len(self._cache),
        }
