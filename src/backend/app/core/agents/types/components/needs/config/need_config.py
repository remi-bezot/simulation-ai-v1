from dataclasses import dataclass
from typing import Dict


@dataclass
class NeedConfig:
    """Configuration globale du système de besoins"""

    MAX_VALUE: float = 100.0
    MIN_VALUE: float = 0.0
    CACHE_SIZE: int = 1000
    HISTORY_SIZE: int = 1000

    THRESHOLDS: Dict[str, float] = {
        "NORMAL": 0.3,
        "WARNING": 0.5,
        "CRITICAL": 0.8,
        "EMERGENCY": 0.9,
    }
