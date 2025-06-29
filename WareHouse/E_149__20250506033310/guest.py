'''
Module defining the Guest class representing a guest with a power attribute.
'''
class Guest:
    def __init__(self, power):
        self.power = power
    def __str__(self):
        return f"Guest(power={self.power})"
    def __repr__(self):
        return self.__str__()