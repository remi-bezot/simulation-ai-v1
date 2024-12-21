from dataclasses import dataclass
from typing import Optional
from ..config.need_config import NeedConfig
from ..validators.need_validator import NeedValidator


@dataclass
class NeedHandler:
    """Gestionnaire des opérations sur les besoins"""

    config: NeedConfig
    validator: NeedValidator

    def process_need(self, need_id: str, value: float) -> Optional[float]:
        if not self.validator.validate(need_id, value):
            return None
        return min(max(value, self.config.MIN_VALUE), self.config.MAX_VALUE)
