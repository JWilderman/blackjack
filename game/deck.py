import random

class deck:
    def __init__(self):
        """"""
        self.hand = []
        self.current_deck = []
        self.total = 0

    def playable(self, points):
        if(points <= 0):
            return False
        else:
            return True

    def getScore(self):
        self.total = 0
        for item in self.hand:
            self.total += item
        for item in self.hand:
            if item == 11:
                if self.total > 21:
                    self.total -= 10

    def create_deck(self):
        new_deck = [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
        new_deck = random.shuffle(new_deck)
        self.current_deck = new_deck

    def hitCard(self, action):
        if action not in ["stand", "split"]:
            self.hand.append(self.current_deck[-1])