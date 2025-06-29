'''
Module containing the Action class to represent actions performed by a person.
'''
class Action:
    def __init__(self, dish_c, dish_d):
        self.dish_c = dish_c
        self.dish_d = dish_d
    def perform(self, dishes):
        dishes[self.dish_c] += 1
        dishes[self.dish_d] += 1