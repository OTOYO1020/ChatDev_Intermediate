'''
Module containing the Condition class to represent conditions with two dishes.
'''
class Condition:
    def __init__(self, dish_a, dish_b):
        self.dish_a = dish_a
        self.dish_b = dish_b
    def is_satisfied(self, dishes):
        return dishes[self.dish_a] > 0 and dishes[self.dish_b] > 0