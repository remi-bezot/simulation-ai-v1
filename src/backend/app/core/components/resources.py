class Resources:
    def __init__(self):
        self.resources = {}

    def add_resource(self, resource: str, quantity: float):
        if resource in self.resources:
            self.resources[resource] += quantity
        else:
            self.resources[resource] = quantity

    def use_resource(self, resource: str, quantity: float):
        if resource in self.resources and self.resources[resource] >= quantity:
            self.resources[resource] -= quantity
            if self.resources[resource] <= 0:
                del self.resources[resource]
