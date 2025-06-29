'''
Input validation module for the Happy People Calculator.
'''
class InputValidation:
    def validate_input(self, n, p, m):
        '''
        Validate the input values for number of people, dish positions, and value of m.
        '''
        if n <= 0:
            raise ValueError("Number of people must be positive.")
        if len(p) != n:
            raise ValueError("Length of dish positions must match number of people.")
        if m <= 0:
            raise ValueError("Value of m must be positive.")
        # Removed the uniqueness check
        return True