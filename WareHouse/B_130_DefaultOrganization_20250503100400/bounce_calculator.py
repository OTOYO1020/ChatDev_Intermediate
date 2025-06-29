'''
Module for calculating the number of bounces based on lengths.
'''
class BounceCalculator:
    '''
    Class to calculate the number of bounces.
    '''
    def __init__(self):
        '''
        Initializes the BounceCalculator.
        '''
        self.current_coordinate = 0
    def calculate_bounces(self, lengths, x):
        '''
        Calculates the number of bounces at coordinates less than or equal to x.
        '''
        if not lengths:  # Check if lengths is empty
            return 0
        bounce_count = 0
        self.current_coordinate = 0  # Reset current_coordinate for each calculation
        for length in lengths:
            self.current_coordinate += length
            if self.current_coordinate <= x:
                bounce_count += 1
        return bounce_count