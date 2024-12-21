class State:
    def __init__(self):
        self.state = {}

    def update_state(self, key: str, value):
        self.state[key] = value

    def get_state(self, key: str):
        return self.state.get(key)
