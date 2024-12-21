from app.core.agents.types.agent_type import AgentType
from app.core.agents.interfaces.i_healer import IHealer
from app.core.agents.healing_resource_manager import HealingResourceManager
from app.core.agents.healing_skills import HealingSkills


class HealerAgentType(AgentType, IHealer):
    """
    Type d'agent pour les soigneurs.
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.healing_resource_manager = HealingResourceManager()
        self.healing_skills = HealingSkills()

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'agent.

        :return: Le nom du type d'agent.
        """
        return "Healer"

    def heal(self, target, healing_amount: float):
        """
        Soigner une cible.

        :param target: La cible à soigner.
        :param healing_amount: La quantité de soin à apporter.
        """
        if self.healing_resource_manager.has_resources(
            {"healing_potion": healing_amount}
        ):
            self.healing_resource_manager.use_resource("healing_potion", healing_amount)
            target.health += healing_amount
            if target.health > 100:
                target.health = 100
            print(
                f"L'agent soigneur soigne {target.name} avec {healing_amount} points de vie"
            )
        else:
            print(
                f"L'agent soigneur n'a pas assez de ressources pour soigner {target.name}"
            )

    def learn_healing_skill(self, skill: str):
        """
        Apprendre une compétence de soin.

        :param skill: La compétence de soin à apprendre.
        """
        self.healing_skills.learn_skill(skill)

    def has_healing_skill(self, skill: str) -> bool:
        """
        Vérifie si l'agent a une compétence de soin.

        :param skill: La compétence de soin à vérifier.
        :return: True si l'agent a la compétence, sinon False.
        """
        return self.healing_skills.has_skill(skill)
