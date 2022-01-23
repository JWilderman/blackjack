import random

class deck:
    """"""
    def __init__(self):
        """"""
        self.hand = []
        self.hand2 = []
        self.current_deck = []
        self.total = 0
        self.total2 = 0
        self.dealer_hand = []
        self.dealer_total = 0
        self.create_deck()

    def getScore(self):
        self.total = 0
        for item in self.hand:
            self.total += item
        for item in self.hand:
            if item == 11:
                if self.total > 21:
                    self.total -= 10

    def hand2Score(self):
        self.total2 = 0
        for item in self.hand2:
            self.total2 += item
        for item in self.hand2:
            if item == 11:
                if self.total2 > 21:
                    self.total2 -= 10
    
    def dealerScore(self):
        self.dealer_total = 0
        for item in self.dealer_hand:
            self.dealer_total += item
        for item in self.dealer_hand:
            if item == 11:
                if self.dealer_total > 21:
                    self.dealer_total -= 10

    def create_deck(self):
        new_deck = [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
        random.shuffle(new_deck)
        self.current_deck = new_deck

    def hitCard(self):
        self.hand.append(self.current_deck.pop())

    def hitCard2(self):
        self.hand2.append(self.current_deck.pop())

    def dealerHit(self):
        self.dealer_hand.append(self.current_deck.pop())
