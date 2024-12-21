from enum import Enum


class NeedCategory(Enum):
    PHYSICAL = "physical"
    MENTAL = "mental"
    SOCIAL = "social"
    ENVIRONMENTAL = "environmental"

    def get_description(self) -> str:
        return {
            self.PHYSICAL: "Besoins physiques fondamentaux",
            self.MENTAL: "Besoins mentaux et cognitifs",
            self.SOCIAL: "Besoins d'interactions sociales",
            self.ENVIRONMENTAL: "Besoins environnementaux",
        }[self]
