from deck import deck

class Actions(deck):
    def __init__(self):
        """"""
    def stand(self, points, bet):
        """"""
        while deck.dealer_total <= 16:
            deck.dealerHit()
            deck.dealerScore()
        if self.dealer_bust():
            if self.bust():
                print("All have gone bust, no bets were lost.")
                return False
            else:
                print("House has gone bust, player has won.")
                points += bet
                return points

    def hit(self):
        """"""
        deck.hitCard()
        deck.getScore()
        self.bust()

    def split(self, points, bet):
        """"""
        if (deck.hand[0] == deck.hand[1]) and (bet*2) <= points:
            self.split_input = input("Would you like to split your hand? [y/n]: ").lower
            deck.hand2.append(deck.hand.pop(-1))
            bet *= 2
            return bet
        else: 
            print("You cannot split your hand.")
            return False

    def double_down(self, points, bet):
        """"""
        if (bet*2) < points:
            return False
        else:
            self.hit()
            bet *= 2
            return bet

    def bust(self):
        """"""
        if deck.total > 21:
            return True

    def dealer_bust(self):
        if deck.dealer_total > 21:
            return True