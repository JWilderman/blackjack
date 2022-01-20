from actions import Actions
from deck import deck

class Handler:
    """"""
    def __init__(self):
        self.keep_playing = True

    def start_game(self):
        """"""
        while self.keep_playing:
            self._outputs()
            
    def _get_inputs(self):
        """"""
        choice = "z"
        while choice.lower() not in ["stand", "hit", "split", "double down"]:
            choice = input("Would you like to hit, stand, double down, or split? ")
        self._updates(choice)
        pass

    def _updates(self, action):
        """"""

    def _outputs(self):
        """"""