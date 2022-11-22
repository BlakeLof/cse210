import random

class Card:


    def __init__(self):
        self.card = 0

    def newCard(self):
        self.card = random.randomint(1, 12)
