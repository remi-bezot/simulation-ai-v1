from dataclasses import dataclass
from typing import Optional
from ..config.need_config import NeedConfig


@dataclass
class NeedValidator:
    """Validateur des besoins"""

    config: NeedConfig

    def validate(self, need_id: str, value: float) -> bool:
        if not isinstance(value, (int, float)):
            return False
        if value < self.config.MIN_VALUE or value > self.config.MAX_VALUE:
            return False
        return True
