from typing import Dict, List, Optional
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Emotions:
    """Classe pour gérer les émotions de l'agent"""

    VALID_EMOTIONS = {
        "joy": {"opposite": "sadness", "threshold": 0.3},
        "sadness": {"opposite": "joy", "threshold": 0.3},
        "anger": {"opposite": "fear", "threshold": 0.4},
        "fear": {"opposite": "anger", "threshold": 0.4},
        "trust": {"opposite": "disgust", "threshold": 0.3},
        "disgust": {"opposite": "trust", "threshold": 0.3},
    }

    current_emotions: Dict[str, float] = field(default_factory=dict)
    emotion_history: List[Dict] = field(default_factory=list)

    def feel_emotion(self, emotion: str, intensity: float) -> bool:
        """
        Ressent une émotion avec une certaine intensité.

        :param emotion: L'émotion à ressentir
        :param intensity: L'intensité de l'émotion (entre 0 et 1)
        :return: True si l'émotion est ressentie, False sinon
        """
        if not self._validate_emotion(emotion, intensity):
            return False

        if emotion not in self.current_emotions:
            self.current_emotions[emotion] = 0

        self.current_emotions[emotion] = min(
            1.0, self.current_emotions[emotion] + intensity
        )
        self._handle_opposite_emotion(emotion)
        self._record_emotion(emotion, intensity)
        return True

    def decay(self, rate: float = 0.1) -> None:
        """
        Fait décroître toutes les émotions.

        :param rate: Taux de décroissance (entre 0 et 1)
        """
        for emotion in list(self.current_emotions.keys()):
            self.current_emotions[emotion] *= 1 - rate
            if self.current_emotions[emotion] < 0.1:
                del self.current_emotions[emotion]

    def get_current(self) -> Dict[str, float]:
        """Retourne les émotions actuelles"""
        return self.current_emotions.copy()

    def get_mood(self) -> float:
        """
        Calcule l'humeur globale.

        :return: Valeur entre -1 (négatif) et 1 (positif)
        """
        positive = sum(self.current_emotions.get(e, 0) for e in ["joy", "trust"])
        negative = sum(
            self.current_emotions.get(e, 0)
            for e in ["sadness", "fear", "anger", "disgust"]
        )

        if not positive and not negative:
            return 0

        return (positive - negative) / (positive + negative)

    def get_dominant_emotion(self) -> Optional[str]:
        """
        Retourne l'émotion dominante.

        :return: Le nom de l'émotion dominante ou None
        """
        if not self.current_emotions:
            return None
        return max(self.current_emotions.items(), key=lambda x: x[1])[0]

    def _validate_emotion(self, emotion: str, intensity: float) -> bool:
        """Valide une émotion et son intensité"""
        if emotion not in self.VALID_EMOTIONS:
            return False
        if not 0 <= intensity <= 1:
            return False
        return True

    def _handle_opposite_emotion(self, emotion: str) -> None:
        """Gère les émotions opposées"""
        opposite = self.VALID_EMOTIONS[emotion]["opposite"]
        if opposite in self.current_emotions:
            self.current_emotions[opposite] *= 0.5

    def _record_emotion(self, emotion: str, intensity: float) -> None:
        """Enregistre une émotion dans l'historique"""
        self.emotion_history.append(
            {"emotion": emotion, "intensity": intensity, "timestamp": datetime.now()}
        )
