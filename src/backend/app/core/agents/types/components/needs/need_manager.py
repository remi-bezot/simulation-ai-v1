from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from datetime import datetime
from statistics import mean

from .enums.need_category import NeedCategory
from .enums.need_urgency import NeedUrgency
from .definitions.need_definitions_registry import NeedDefinitionsRegistry
from .tracking.need_history import NeedHistory


@dataclass
class NeedManager:
    current_needs: Dict[str, float] = field(
        default_factory=lambda: {
            need: 0.0 for need in NeedDefinitionsRegistry.VALID_NEEDS.keys()
        }
    )
    history: NeedHistory = field(default_factory=NeedHistory)

    # ... méthodes de gestion des besoins ...
