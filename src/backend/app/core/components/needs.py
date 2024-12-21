class Needs:
    def __init__(self):
        self.needs = {}

    def satisfy_need(self, need: str, amount: float):
        if need in self.needs:
            self.needs[need] -= amount

    def increase_need(self, need: str, amount: float):
        if need in self.needs:
            self.needs[need] += amount
        else:
            self.needs[need] = amount

    def is_need_satisfied(self, need: str) -> bool:
        return self.needs.get(need, 0) <= 0
