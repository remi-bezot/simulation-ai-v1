from dataclasses import dataclass
from typing import List
from ..definitions.need_definition import NeedDefinition
from ..exceptions.need_registry_exception import NeedRegistryException


@dataclass
class NeedDefinitionValidator:
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
