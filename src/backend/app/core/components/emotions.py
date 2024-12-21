from typing import Dict, Optional
from enum import Enum


class EmotionType(Enum):
    JOIE = "joie"
    TRISTESSE = "tristesse"
    COLERE = "colere"
    PEUR = "peur"
    SURPRISE = "surprise"
    DEGOUT = "degout"


class Emotions:
    def __init__(self):
        self.emotions: Dict[str, float] = {}
        self.decay_rate: float = 0.1
        self.max_intensity: float = 1.0

    def feel_emotion(self, emotion: str, intensity: float):
        self.emotions[emotion] = intensity

    def reduce_emotion(self, emotion: str, amount: float):
        if emotion in self.emotions:
            self.emotions[emotion] -= amount
            if self.emotions[emotion] <= 0:
                del self.emotions[emotion]

    def remove_emotion(self, emotion: str):
        if emotion in self.emotions:
            del self.emotions[emotion]

    def decay(self, delta_time: float = 1.0):
        """Diminue l'intensité des émotions avec le temps"""
        for emotion in list(self.emotions.keys()):
            self.reduce_emotion(emotion, self.decay_rate * delta_time)

    def get_mood(self) -> float:
        """Calcule l'humeur générale basée sur les émotions"""
        if not self.emotions:
            return 0.0
        positive = sum(
            self.emotions[e] for e in self.emotions if e in [EmotionType.JOIE.value]
        )
        negative = sum(
            self.emotions[e]
            for e in self.emotions
            if e in [EmotionType.TRISTESSE.value, EmotionType.COLERE.value]
        )
        return (positive - negative) / self.max_intensity

    def get_dominant_emotion(self) -> Optional[str]:
        """Retourne l'émotion dominante"""
        if not self.emotions:
            return None
        return max(self.emotions.items(), key=lambda x: x[1])[0]

    def get_emotion_intensity(self, emotion: str) -> float:
        """Retourne l'intensité d'une émotion spécifique"""
        return self.emotions.get(emotion, 0.0)

    def update_from_interaction(self, interaction_type: str):
        """Met à jour les émotions basées sur une interaction"""
        if interaction_type == "positive":
            self.feel_emotion(EmotionType.JOIE.value, 0.5)
            self.reduce_emotion(EmotionType.TRISTESSE.value, 0.2)
        elif interaction_type == "negative":
            self.feel_emotion(EmotionType.COLERE.value, 0.5)
            self.feel_emotion(EmotionType.TRISTESSE.value, 0.3)

    def get_current(self) -> Dict[str, float]:
        """Retourne l'état émotionnel actuel"""
        return self.emotions.copy()

    def is_emotional(self) -> bool:
        """Vérifie si l'agent est dans un état émotionnel intense"""
        return any(intensity > 0.7 for intensity in self.emotions.values())

    def reset(self):
        """Réinitialise toutes les émotions"""
        self.emotions.clear()
