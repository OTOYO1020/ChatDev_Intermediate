'''
Contains the DataProcessor class that handles data manipulation and calculations.
'''
class DataProcessor:
    def __init__(self):
        self.current_sequence = []  # Initialize current_sequence
    def set_sequence(self, sequence):
        self.current_sequence = sequence.copy()  # Store a copy of the original sequence
    def replace_and_sum(self, b, c):
        '''
        Replace occurrences of b with c in the current sequence,
        and return the sum of the modified sequence.
        '''
        # Replace occurrences of b with c in the current_sequence
        self.current_sequence = [c if x == b else x for x in self.current_sequence]
        # Calculate the sum of the modified sequence
        return sum(self.current_sequence)  # Return the sum of the modified sequence