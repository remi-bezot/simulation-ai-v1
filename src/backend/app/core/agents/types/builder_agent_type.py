from app.core.agents.types.agent_type import AgentType
from app.core.agents.interfaces.i_builder import IBuilder
from app.core.agents.resource_manager import ResourceManager
from app.core.agents.construction_skills import ConstructionSkills


class BuilderAgentType(AgentType, IBuilder):
    """
    Type d'agent pour les constructeurs.
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.resource_manager = ResourceManager()
        self.construction_skills = ConstructionSkills()

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'agent.

        :return: Le nom du type d'agent.
        """
        return "Builder"

    def build_structure(self, structure_type: str, required_resources: dict):
        """
        Construire une structure.

        :param structure_type: Le type de structure à construire.
        :param required_resources: Les ressources nécessaires pour construire la structure.
        """
        if self.resource_manager.has_resources(required_resources):
            self.resource_manager.use_resource(required_resources)
            print(f"L'agent constructeur construit une {structure_type}")
        else:
            print(
                f"L'agent constructeur n'a pas assez de ressources pour construire une {structure_type}"
            )

    def learn_construction_skill(self, skill: str):
        """
        Apprendre une compétence de construction.

        :param skill: La compétence de construction à apprendre.
        """
        self.construction_skills.learn_skill(skill)

    def has_construction_skill(self, skill: str) -> bool:
        """
        Vérifie si l'agent a une compétence de construction.

        :param skill: La compétence de construction à vérifier.
        :return: True si l'agent a la compétence, sinon False.
        """
        return self.construction_skills.has_skill(skill)

    def collaborate_with(self, other_agent, project: str):
        """
        Collaborer avec un autre agent pour un projet de construction.

        :param other_agent: L'autre agent avec lequel collaborer.
        :param project: Le projet de construction.
        """
        print(
            f"L'agent constructeur collabore avec {other_agent} sur le projet {project}"
        )
