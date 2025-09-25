from .divvy import Divvy

class DivvyUp(Divvy):
    """
    DivvyUp class inherits from Divvy and provides functionality for splitting expenses based on individual contributions.
    """

    def __init__(self):
        super().__init__()
