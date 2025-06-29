'''
Module to handle string input for the prefix checking application.
'''
class StringInput:
    '''
    Class to handle string input for the prefix checking application.
    '''
    def get_strings(self):
        s = input("Please enter the first string (S) to check as a prefix: ")
        t = input("Please enter the second string (T) to check against: ")
        return s, t