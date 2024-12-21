class WorkSkills:
    def __init__(self):
        self.skills = []
        self.energy = 100
        self.experience = {}

    def learn_skill(self, skill: str):
        self.skills.append(skill)
        self.experience[skill] = 0

    def has_skill(self, skill: str) -> bool:
        return skill in self.skills

    def gain_experience(self, skill: str, amount: float):
        if skill in self.experience:
            self.experience[skill] += amount

    def get_skill_level(self, skill: str) -> float:
        return self.experience.get(skill, 0)

    def use_energy(self, amount: float):
        self.energy -= amount
        if self.energy < 0:
            self.energy = 0

    def restore_energy(self, amount: float):
        self.energy += amount
        if self.energy > 100:
            self.energy = 100
