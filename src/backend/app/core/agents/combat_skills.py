class CombatSkills:
    def __init__(self):
        self.skills = []

    def learn_skill(self, skill: str):
        self.skills.append(skill)

    def has_skill(self, skill: str) -> bool:
        return skill in self.skills

    def remove_skill(self, skill: str):
        if skill in self.skills:
            self.skills.remove(skill)
