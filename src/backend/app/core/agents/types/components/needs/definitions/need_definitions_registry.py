from typing import Dict, List, Optional
from dataclasses import dataclass, field
from ..enums.need_category import NeedCategory
from ..interfaces.i_need_registry import INeedRegistry
from ..validators.need_definition_validator import NeedDefinitionValidator
from ..observers.need_registry_observer import INeedRegistryObserver
from ..exceptions.need_registry_exception import NeedRegistryException
from .need_definition import NeedDefinition


@dataclass
class NeedDefinitionsRegistry(INeedRegistry):
    """Registre des définitions des besoins avec validation intégrée"""

    _validator: NeedDefinitionValidator = field(default_factory=NeedDefinitionValidator)
    _observers: List[INeedRegistryObserver] = field(default_factory=list)

    VALID_NEEDS: Dict[str, NeedDefinition] = {
        "hunger": NeedDefinition(
            category=NeedCategory.PHYSICAL,
            threshold=80,
            decay_rate=0.1,
            impact_on_mood=-0.2,
            recovery_rate=0.05,
            description="Niveau de faim de l'agent",
            priority=1,
        ),
        # ... autres besoins physiques ...
    }

    def register_need(self, name: str, definition: NeedDefinition) -> None:
        """Enregistre un nouveau besoin"""
        try:
            self._validator.validate(definition)
            self.VALID_NEEDS[name] = definition
            self._notify_observers("add", name, definition)
        except Exception as e:
            raise NeedRegistryException(f"Erreur d'enregistrement: {str(e)}")

    def get_need(self, name: str) -> Optional[NeedDefinition]:
        """Récupère la définition d'un besoin"""
        return self.VALID_NEEDS.get(name)

    def get_needs_by_category(
        self, category: NeedCategory
    ) -> Dict[str, NeedDefinition]:
        """Retourne les besoins filtrés par catégorie"""
        return {
            name: need
            for name, need in self.VALID_NEEDS.items()
            if need.category == category
        }

    def get_priority_needs(self, limit: Optional[int] = None) -> List[str]:
        """Retourne les besoins triés par priorité"""
        sorted_needs = sorted(
            self.VALID_NEEDS.items(), key=lambda x: (x[1].priority, x[0])
        )
        return (
            [name for name, _ in sorted_needs[:limit]]
            if limit
            else [name for name, _ in sorted_needs]
        )

    def add_observer(self, observer: INeedRegistryObserver) -> None:
        """Ajoute un observateur"""
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: INeedRegistryObserver) -> None:
        """Supprime un observateur"""
        if observer in self._observers:
            self._observers.remove(observer)

    def _notify_observers(
        self, action: str, name: str, definition: NeedDefinition
    ) -> None:
        """Notifie les observateurs d'un changement"""
        for observer in self._observers:
            observer.on_registry_change(action, name, definition)
            self._notify_specific_observer(observer, action, name, definition)

    def _notify_specific_observer(
        self,
        observer: INeedRegistryObserver,
        action: str,
        name: str,
        definition: NeedDefinition,
    ) -> None:
        """Notifie un observateur spécifique en fonction de l'action"""
        if action == "add":
            observer.on_need_added(name, definition)
        elif action == "update":
            observer.on_need_updated(name, definition)
        elif action == "remove":
            observer.on_need_removed(name)
