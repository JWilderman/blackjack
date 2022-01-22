from deck import deck

class Actions(deck):
    """"""
    def __init__(self):
        """"""
    def stand(self, points, bet):
        """"""
        while deck.dealer_total <= 16:
            deck.dealerHit()
            deck.dealerScore()
        if self.dealer_bust():
            if self.bust() and self.bust2():
                print("All have gone bust, no bets were lost.")
                return False
            elif (self.bust() == False and self.bust2() == True) or (self.bust() == True and self.bust2() == False):
                print("House has gone bust, but one of the player's hands have won.")
                points += bet/2
                return points
            else:
                print("House has gone bust, player has won.")
                points += bet
                return points

    def hit(self):
        """"""
        deck.hitCard()
        deck.getScore()
        self.bust()
        if len(deck.current_deck) == 0:
            deck.create_deck()

    def hit2(self):
        """"""
        deck.hitCard2()
        deck.hand2Score()
        self.bust2()
        if len(deck.current_deck) == 0:
            deck.create_deck()

    def hit_d(self):
        """"""
        deck.dealerHit()
        deck.dealerScore()
        self.dealer_bust()
        if len(deck.current_deck) == 0:
            deck.create_deck()

    def split(self, points, bet):
        """"""
        if (deck.hand[0] == deck.hand[1]) and (bet*2) <= points:
            self.split_input = input("Would you like to split your hand? [y/n]: ").lower()
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

    def double_down2(self, points, bet):
        """"""
        if (bet*1.5) < points:
            return False
        else:
            self.hit2()
            bet *= 1.5
            return bet    

    def bust(self):
        """"""
        if deck.total > 21:
            return True
        return False

    def bust2(self):
        """"""
        if deck.total2 > 21:
            return True
        return False

    def dealer_bust(self):
        if deck.dealer_total > 21:
            return True
        return False