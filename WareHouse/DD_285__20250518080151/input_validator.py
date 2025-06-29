'''
Contains the logic for validating user input.
'''
class InputValidator:
    @staticmethod
    def validate_input(N: int, S: list, T: list) -> bool:
        # Validate the number of users and the length of handles lists
        if N <= 0 or len(S) != N or len(T) != N:
            return False
        return True