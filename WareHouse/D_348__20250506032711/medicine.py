'''
Module to handle medicine representation.
'''
class Medicine:
    def __init__(self, row, col, energy):
        self.position = (row, col)
        self.energy = energy