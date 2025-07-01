'''
Module containing the string modification logic.
'''
class StringModifier:
    '''
    Class to handle string modification operations.
    '''
    def __init__(self, initial_string):
        '''
        Initialize with the initial string.
        '''
        self.string = initial_string
    def replace_character(self, c_i, d_i):
        '''
        Replace all occurrences of character c_i with character d_i in the string.
        '''
        self.string = self.string.replace(c_i, d_i)
    def get_modified_string(self):
        '''
        Return the modified string.
        '''
        return self.string