class MultiverseNotFoundError(Exception):
    """
    Exception levée lorsqu'un multivers n'est pas trouvé.
    """

    def __init__(self, multiverse_id: int):
        super().__init__(f"Aucun multivers trouvé avec l'ID {multiverse_id}.")
        self.multiverse_id = multiverse_id


class UniverseNotFoundError(Exception):
    """
    Exception levée lorsqu'un univers n'est pas trouvé.
    """

    def __init__(self, universe_id: int):
        super().__init__(f"Aucun univers trouvé avec l'ID {universe_id}.")
        self.universe_id = universe_id
