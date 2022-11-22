import random
"""This class is just to create a new card and return it to the game class"""
class Card:

    def __init__(self):
        self.card = 0

    def newCard(self):
        return random.randomint(1, 12)
