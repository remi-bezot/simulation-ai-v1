from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
from ..interfaces.i_need_recorder import INeedRecorder


@dataclass
class NeedRecorder(INeedRecorder):
    """Enregistreur d'historique des besoins"""

    history: List[Dict] = field(default_factory=list)
    max_history_size: int = 1000

    def record_change(self, need: str, value: float, timestamp: datetime) -> None:
        """Enregistre un changement de besoin"""
        if len(self.history) >= self.max_history_size:
            self.history.pop(0)

        self.history.append({"need": need, "value": value, "timestamp": timestamp})

    def get_history(self, need: str) -> List[Dict]:
        """Récupère l'historique d'un besoin"""
        return [record for record in self.history if record["need"] == need]

    def get_last_value(self, need: str) -> Optional[float]:
        """Récupère la dernière valeur d'un besoin"""
        history = self.get_history(need)
        return history[-1]["value"] if history else None

    def clear_history(self, need: Optional[str] = None) -> None:
        """Efface l'historique"""
        if need:
            self.history = [record for record in self.history if record["need"] != need]
        else:
            self.history.clear()

    def get_history_size(self) -> int:
        """Retourne la taille de l'historique"""
        return len(self.history)

    def get_needs_with_history(self) -> List[str]:
        """Retourne la liste des besoins ayant un historique"""
        return list(set(record["need"] for record in self.history))
