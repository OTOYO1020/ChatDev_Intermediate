'''
Module for character replacement logic.
'''
class CharacterReplacer:
    '''
    Class to handle character replacement in a string.
    '''
    def __init__(self, input_string, pairs):
        '''
        Initializes the CharacterReplacer with the input string and pairs of characters.
        '''
        self.input_string = input_string
        self.pairs = pairs
    def perform_replacements(self):
        '''
        Performs the character replacements based on the provided pairs in order.
        '''
        modified_string = self.input_string
        # Perform replacements in order
        for c_i, d_i in self.pairs:
            # Use a temporary string to avoid conflicts
            modified_string = modified_string.replace(c_i, d_i)
        return modified_string