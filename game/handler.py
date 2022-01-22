from argparse import Action
from actions import Actions
from deck import deck

class Handler:
    """"""
    def __init__(self):
        self.keep_playing = True
        self.points = 300
        self.bet = 0

    def start_game(self):
        """"""
        while self.points > 0:
            self._outputs()
            
    def _get_inputs(self):
        """"""
        while self.bet == 0 or self.bet > self.points:
            self.bet = int(input("How much points would you like to bet? "))
            if self.bet > self.points or self.bet == 0:
                print("Invalid bet amount.")
        choice = "z"
        if len(deck.hand2) == 0:
            while choice not in ["stand", "hit", "split", "double down"]:
                choice = input("Would you like to hit, stand, double down, or split? ").lower()
            self._updates(choice)
        else:
            print("Your Hands: " + deck.hand + " " + deck.hand2)
            while choice not in ["stand", "hit", "split", "double down"]:
                choice = input("Would you like to hit, stand, double down, or split for your first hand? ").lower()
            self._updates(choice)
            while choice not in ["stand", "hit", "split", "double down"]:
                choice = input("Would you like to hit, stand, double down, or split for your second hand? ").lower() + "2"
            self._updates(choice)
        pass

    def _updates(self, action):
        """"""
        if action == "split":
            if Actions.split(self.points, self.bet) == False:
                print("You are unable to split.")
            else:
                self.bet = Actions.split(self.points, self.bet)
        
        if action == "double down":
            if Actions.double_down(self.points, self.bet) == False:
                print("You are unable to double down.")
            else:
                self.bet = Actions.double_down(self.points, self.bet)

        if action == "double down2":
            if Actions.double_down2(self.points, self.bet) == False:
                print("You are unable to double down.")
            else:
                self.bet = Actions.double_down2(self.points, self.bet)

        if action == "hit":
            Actions.hit()

        if action == "hit2":
            Actions.hit2()

        if action == "stand" or action == "stand2":
            if Actions.stand(self.points, self.bet) == False:
                pass
            else: 
                self.points = Actions.stand(self.points, self.bet)
        
        if Actions.bust():
            self.points -= self.bet
        if len(deck.hand2) > 0:
            if Actions.bust2():
                self.points -= self.bet


    def _outputs(self):
        """"""
        deck.hitCard
        deck.dealerHit
        deck.hitCard
        deck.dealerHit
        print("Dealer's Hand: [X," + deck.dealer_hand(-1) + "]")
        if len(deck.hand2) == 0:
            print("Your Hand: " + deck.hand)
        else:
            print("Your Hands: " + deck.hand + " " + deck.hand2)
        self._get_inputs()