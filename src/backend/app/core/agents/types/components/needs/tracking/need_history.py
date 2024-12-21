from dataclasses import dataclass, field
from typing import Dict, List
from datetime import datetime


@dataclass
class NeedHistory:
    needs_history: List[Dict] = field(default_factory=list)
    need_satisfaction_stats: Dict[str, List[float]] = field(default_factory=dict)

    def record_need(self, need: str, value: float) -> None:
        self.needs_history.append(
            {"need": need, "value": value, "timestamp": datetime.now()}
        )
