from app.core.agents.types.agent_type import AgentType
from app.core.agents.interfaces.i_worker import IWorker
from app.core.agents.work_skills import WorkSkills


class WorkerAgentType(AgentType, IWorker):
    """
    Type d'agent pour les travailleurs.
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.work_skills = WorkSkills()

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'agent.

        :return: Le nom du type d'agent.
        """
        return "Worker"

    def work(self, task: str, duration: int):
        """
        Effectuer une tâche pendant une durée donnée.

        :param task: La tâche à effectuer
        :param duration: La durée du travail
        """
        if self.work_skills.energy < 20:
            print(f"L'agent {self.name} est trop fatigué pour travailler")
            return False

        if not self.work_skills.has_skill(task):
            print(f"L'agent {self.name} n'a pas la compétence {task}")
            return False

        self.work_skills.use_energy(duration * 0.1)
        self.work_skills.gain_experience(task, duration * 0.05)
        print(f"L'agent {self.name} travaille sur {task} pendant {duration} minutes")
        return True

    def take_break(self, duration: int):
        """
        Prendre une pause pour récupérer de l'énergie.

        :param duration: La durée de la pause
        """
        energy_recovered = duration * 0.2
        self.work_skills.restore_energy(energy_recovered)
        print(
            f"L'agent {self.name} prend une pause de {duration} minutes et récupère {energy_recovered} points d'énergie"
        )

    def learn_work_skill(self, skill: str):
        """
        Apprendre une compétence de travail.

        :param skill: La compétence à apprendre
        """
        self.work_skills.learn_skill(skill)
        print(f"L'agent {self.name} apprend la compétence {skill}")

    def get_skill_level(self, skill: str) -> float:
        """
        Obtenir le niveau d'une compétence.

        :param skill: La compétence à vérifier
        :return: Le niveau de la compétence
        """
        return self.work_skills.get_skill_level(skill)
