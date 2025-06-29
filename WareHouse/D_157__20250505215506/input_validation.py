'''
Utility class for validating user inputs.
'''
class InputValidation:
    @staticmethod
    def validate_integer(value):
        try:
            int(value)
            return True
        except ValueError:
            return False