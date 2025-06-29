'''
Module for input validation utilities.
'''
class InputValidation:
    @staticmethod
    def validate_integer(value):
        '''
        Validates if the provided value can be converted to an integer.
        Parameters:
        value (str): The value to validate.
        Returns:
        bool: True if the value is a valid integer, False otherwise.
        '''
        try:
            int(value)
            return True
        except ValueError:
            return False