from app.core.agents.types.agent_type import AgentType
from app.core.agents.interfaces.i_soldier import ISoldier
from app.core.agents.combat_skills import CombatSkills


class SoldierAgentType(AgentType, ISoldier):
    """
    Type d'agent pour les soldats.
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.combat_skills = CombatSkills()

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'agent.

        :return: Le nom du type d'agent.
        """
        return "Soldier"

    def attack(self, target):
        """
        Attaquer une cible.

        :param target: La cible à attaquer.
        """
        if self.has_combat_skill("attack"):
            print(f"L'agent soldat attaque {target.name}")
        else:
            print(
                f"L'agent soldat n'a pas les compétences nécessaires pour attaquer {target.name}"
            )

    def defend(self):
        """
        Défendre contre une attaque.
        """
        if self.has_combat_skill("defend"):
            print("L'agent soldat se défend contre une attaque")
        else:
            print("L'agent soldat n'a pas les compétences nécessaires pour se défendre")

    def learn_combat_skill(self, skill: str):
        """
        Apprendre une compétence de combat.

        :param skill: La compétence de combat à apprendre.
        """
        self.combat_skills.learn_skill(skill)

    def has_combat_skill(self, skill: str) -> bool:
        """
        Vérifie si l'agent a une compétence de combat.

        :param skill: La compétence de combat à vérifier.
        :return: True si l'agent a la compétence, sinon False.
        """
        return self.combat_skills.has_skill(skill)
