from actions import Actions
from deck import deck

class Handler:
    """"""
    def __init__(self):
        self.keep_playing = True
        self.points = 300

    def start_game(self):
        """"""
        while self.points > 0:
            self._outputs()
            
    def _get_inputs(self):
        """"""
        deck.hand.append(deck.current_deck.pop(-1))
        deck.dealer_hand.append(deck.current_deck.pop(-1))
        deck.hand.append(deck.current_deck.pop(-1))
        deck.dealer_hand.append(deck.current_deck.pop(-1))
        print("Dealer's Hand: [X," + deck.dealer_hand(-1) + "]")
        if len(deck.hand2) == 0:
            print("Your Hand: " + deck.hand)
        else:
            print("Your Hands: " + deck.hand + " " + deck.hand2)
        choice = "z"
        if len(deck.hand2) == 0:
            while choice.lower() not in ["stand", "hit", "split", "double down"]:
                choice = input("Would you like to hit, stand, double down, or split? ")
            self._updates(choice)
        else:
            print("Your Hands: " + deck.hand + " " + deck.hand2)
            while choice.lower() not in ["stand", "hit", "split", "double down"]:
                choice = input("Would you like to hit, stand, double down, or split for your first hand? ")
            self._updates(choice)
            while choice.lower() not in ["stand", "hit", "split", "double down"]:
                choice = input("Would you like to hit, stand, double down, or split for your second hand? ")
            self._updates(choice)
        pass

    def _updates(self, action):
        """"""

    def _outputs(self):
        """"""