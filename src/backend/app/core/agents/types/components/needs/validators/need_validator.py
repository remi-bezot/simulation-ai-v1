from dataclasses import dataclass
from typing import List, Optional
from ..exceptions.need_validation_exception import NeedValidationException
from ..config.need_config import NeedConfig
from ..definitions.need_definition import NeedDefinition
from ..exceptions.need_registry_exception import NeedRegistryException


@dataclass
class NeedValidator:
    """Validateur des besoins avec règles configurables"""

    config: NeedConfig

    def validate(self, need_id: str, value: float) -> bool:
        """
        Valide une valeur de besoin
        :raises NeedValidationException: Si la validation échoue
        """
        errors: List[str] = []

        if not isinstance(value, (int, float)):
            errors.append(f"La valeur doit être numérique, reçu: {type(value)}")

        if not self.config.MIN_VALUE <= value <= self.config.MAX_VALUE:
            errors.append(
                f"La valeur doit être entre {self.config.MIN_VALUE} et {self.config.MAX_VALUE}"
            )

        if errors:
            raise NeedValidationException("\n".join(errors), need_id, value)

        return True

    def validate_silent(self, need_id: str, value: float) -> bool:
        """Version silencieuse de la validation qui ne lève pas d'exception"""
        try:
            return self.validate(need_id, value)
        except NeedValidationException:
            return False

    def validate(self, definition: NeedDefinition) -> None:
        errors: List[str] = []

        if not 0 <= definition.threshold <= 100:
            errors.append("Le seuil doit être entre 0 et 100")
        if not 0 <= definition.decay_rate <= 1:
            errors.append("Le taux de décroissance doit être entre 0 et 1")
        if not -1 <= definition.impact_on_mood <= 1:
            errors.append("L'impact sur l'humeur doit être entre -1 et 1")
        if not 0 <= definition.recovery_rate <= 1:
            errors.append("Le taux de récupération doit être entre 0 et 1")

        if errors:
            raise NeedRegistryException("\n".join(errors))
