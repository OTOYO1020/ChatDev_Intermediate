'''
Module representing a card in the card game.
'''
class Card:
    def __init__(self, index):
        self.index = index
        self.value = None  # Initially, the value is unknown