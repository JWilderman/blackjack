from game.deck import deck

class Actions(deck):
    """"""
    def __init__(self):
        """"""
        self.deck = deck()
        self.points = 0
        self.bet = 0

    def starting_deal(self):
        self.deck.dealer_hand = []
        self.deck.hand = []
        self.deck.hand2 = []
        self.deck.hitCard()
        self.deck.dealerHit()
        self.deck.hitCard()
        self.deck.dealerHit()

    def stand(self, points, bet):
        """"""
        while self.deck.dealer_total <= 16:
            self.deck.dealerHit()
            self.deck.dealerScore()
        if self.dealer_bust():
            if self.bust() and self.bust2():
                print("All have gone bust, no bets were lost.")
                self.starting_deal()
                return False
            elif (self.bust() == False and self.bust2() == True) or (self.bust() == True and self.bust2() == False):
                print("House has gone bust, but one of the player's hands have won.")
                points += bet/2
                self.starting_deal()
                return points
            else:
                print("House has gone bust, player has won.")
                points += bet
                self.starting_deal()
                return points
        self.starting_deal

    def hit(self, points, bet):
        """"""
        self.points = points
        self.bet = bet
        self.deck.hitCard()
        self.deck.getScore()
        if self.bust():
            self.stand(self.points, self.bet)
        if len(self.deck.current_deck) == 0:
            self.deck.create_deck()

    def hit2(self, points, bet):
        """"""
        self.deck.hitCard2()
        self.deck.hand2Score()
        if self.bust2():
            self.stand(self.points, self.bet)
        if len(self.deck.current_deck) == 0:
            self.deck.create_deck()

    def hit_d(self):
        """"""
        self.deck.dealerHit()
        self.deck.dealerScore()
        self.dealer_bust()
        if len(self.deck.current_deck) == 0:
            self.deck.create_deck()

    def split(self, points, bet):
        """"""
        if (self.deck.hand[0] == self.deck.hand[-1]) and (bet*2) <= points:
            self.split_input = input("Would you like to split your hand? [y/n]: ").lower()
            self.deck.hand2.append(self.deck.hand.pop(-1))
            bet *= 2
            if self.bust():
                self.stand(self.points, self.bet)
            return bet
        else: 
            print("You cannot split your hand.")
            return False

    def double_down(self, points, bet):
        """"""
        if (bet*2) >= points:
            self.hit(points, bet)
            bet *= 2
            if self.bust():
                self.stand(self.points, self.bet)
            return bet
        else:
            return False
            

    def double_down2(self, points, bet):
        """"""
        if (bet*1.5) >= points:
            self.hit2(points, bet)
            bet *= 1.5
            if self.bust2():
                self.stand(self.points, self.bet)
            return bet
        else:
            return False  

    def bust(self):
        """"""
        if self.deck.total > 21:
            self.deck.hand = []
            return True
        return False

    def bust2(self):
        """"""
        if self.deck.total2 > 21:
            self.deck.hand2 = []
            return True
            
        return False

    def dealer_bust(self):
        if self.deck.dealer_total > 21:
            self.deck.dealer_hand = []
            return True
        return False