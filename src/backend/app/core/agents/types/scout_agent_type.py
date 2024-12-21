from app.core.agents.types.agent_type import AgentType
from app.core.agents.interfaces.i_scout import IScout
from app.core.agents.scouting_skills import ScoutingSkills


class ScoutAgentType(AgentType, IScout):
    """
    Type d'agent pour les éclaireurs.
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.scouting_skills = ScoutingSkills()

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'agent.

        :return: Le nom du type d'agent.
        """
        return "Scout"

    def scout_area(self, area: str):
        """
        Effectuer une reconnaissance d'une zone.

        :param area: La zone à reconnaître.
        """
        if self.has_scouting_skill("scouting"):
            print(f"L'agent éclaireur effectue une reconnaissance de la zone {area}")
        else:
            print(
                f"L'agent éclaireur n'a pas les compétences nécessaires pour reconnaître la zone {area}"
            )

    def learn_scouting_skill(self, skill: str):
        """
        Apprendre une compétence de reconnaissance.

        :param skill: La compétence de reconnaissance à apprendre.
        """
        self.scouting_skills.learn_skill(skill)

    def has_scouting_skill(self, skill: str) -> bool:
        """
        Vérifie si l'agent a une compétence de reconnaissance.

        :param skill: La compétence de reconnaissance à vérifier.
        :return: True si l'agent a la compétence, sinon False.
        """
        return self.scouting_skills.has_skill(skill)
