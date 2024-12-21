from enum import Enum


class NeedUrgency(Enum):
    NORMAL = "normal"
    WARNING = "warning"
    CRITICAL = "critical"
    EMERGENCY = "emergency"

    def get_threshold(self) -> float:
        return {
            self.NORMAL: 0.3,
            self.WARNING: 0.5,
            self.CRITICAL: 0.8,
            self.EMERGENCY: 0.9,
        }[self]
