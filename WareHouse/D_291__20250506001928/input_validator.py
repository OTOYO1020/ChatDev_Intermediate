'''
Module for input validation utilities.
'''
class InputValidator:
    def validate_integer(self, value):
        try:
            num = int(value)
            if num <= 0:
                raise ValueError("Number of cards must be a positive integer.")
            return num
        except ValueError:
            raise ValueError("Invalid input. Please enter a valid integer.")