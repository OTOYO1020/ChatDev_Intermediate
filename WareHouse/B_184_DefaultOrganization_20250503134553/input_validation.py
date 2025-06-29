'''
Module for input validation functions.
'''
class InputValidation:
    @staticmethod
    def validate_integer(value):
        """
        Validate if the given value can be converted to an integer.
        Parameters:
        value (str): The value to validate.
        Returns:
        bool: True if valid integer, False otherwise.
        """
        try:
            int(value)
            return True
        except ValueError:
            return False
    @staticmethod
    def validate_string(value):
        """
        Validate if the given string contains only 'o' and 'x'.
        Parameters:
        value (str): The string to validate.
        Returns:
        bool: True if valid string, False otherwise.
        """
        return all(char in 'ox' for char in value)