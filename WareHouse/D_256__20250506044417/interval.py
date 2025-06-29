'''
Module defining the Interval class for representing intervals.
'''
class Interval:
    def __init__(self, start, end):
        """
        Initializes an Interval object.
        Parameters:
        start (int): The starting point of the interval.
        end (int): The ending point of the interval.
        """
        self.start = start
        self.end = end