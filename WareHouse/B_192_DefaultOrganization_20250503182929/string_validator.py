'''
Module for validating strings based on hard-to-read criteria.
'''
class StringValidator:
    def __init__(self, input_string):
        if len(input_string) < 1 or len(input_string) > 1000:
            raise ValueError("Input string must be between 1 and 1000 characters.")
        self.input_string = input_string
        self.length = len(input_string)
    def check_hard_to_read(self):  # Method to check if the string is hard to read
        """
        Checks if the string alternates between uppercase and lowercase letters.
        Uppercase letters are expected at even indices and lowercase letters at odd indices.
        Returns True if the string meets the criteria, otherwise returns False.
        """
        for index, char in enumerate(self.input_string):
            if index % 2 == 0:  # Even index
                if not char.isupper():
                    return False  # Return False immediately if not uppercase
            else:  # Odd index
                if not char.islower():
                    return False  # Return False immediately if not lowercase
        return True  # Return True if all checks pass