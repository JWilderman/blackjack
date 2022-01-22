from game.actions import Actions
from game.deck import deck

class Handler():
    """"""
    def __init__(self):
        self.keep_playing = True
        self.points = 300
        self.bet = 0
        self.acts = Actions()

    def start_game(self):
        """"""
        self.acts.starting_deal()
        while self.points > 0:
            self._outputs()
            
    def _get_inputs(self):
        """"""
        while self.bet <= 0 or self.bet > self.points:
            self.bet = int(input("How much points would you like to bet? "))
            if self.bet > self.points or self.bet == 0:
                print("Invalid bet amount.")
        choice = "z"
        if len(self.acts.deck.hand2) == 0:
            while choice not in ["stand", "hit", "split", "double down"]:
                choice = input("Would you like to hit, stand, double down, or split? ").lower()
            self._updates(choice)
        else:
            while choice not in ["stand", "hit", "split", "double down"]:
                choice = input("Would you like to hit, stand, double down, or split for your first hand? ").lower()
            self._updates(choice)
            while choice not in ["stand2", "hit2", "split2", "double down2"]:
                choice = input("Would you like to hit, stand, double down, or split for your second hand? ").lower() + "2"
            self._updates(choice)
        pass

    def _updates(self, action):
        """"""
        if action == "split":
            if self.acts.split(self.points, self.bet) == False:
                print("You are unable to split.")
            else:
                self.bet = self.acts.split(self.points, self.bet)
        
        if action == "double down":
            if self.acts.double_down(self.points, self.bet) == False:
                print("You are unable to double down.")
            else:
                self.bet = self.acts.double_down(self.points, self.bet)

        if action == "double down2":
            if self.acts.double_down2(self.points, self.bet) == False:
                print("You are unable to double down.")
            else:
                self.bet = self.acts.double_down2(self.points, self.bet)

        if action == "hit":
            self.acts.hit(self.points, self.bet)

        if action == "hit2":
            self.acts.hit2(self.points, self.bet)

        if action == "stand" or action == "stand2":
            if self.acts.stand(self.points, self.bet) == False:
                pass
            else: 
                self.points = self.acts.stand(self.points, self.bet)

    def _outputs(self):
        """"""
        print("Dealer's Hand: [X, " + str(self.acts.deck.dealer_hand[1:])[1:-2] + "]")
        if len(self.acts.deck.hand2) == 0:
            print("Your Hand: " + str(self.acts.deck.hand))
        else:
            print("Your Hands: " + str(self.acts.deck.hand) + " " + str(self.acts.deck.hand2))
        self._get_inputs()