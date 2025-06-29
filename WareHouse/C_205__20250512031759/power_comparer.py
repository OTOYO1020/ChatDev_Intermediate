'''
Contains the logic for comparing powers of two integers.
'''
from utils import custom_pow
class PowerComparer:
    def compare_powers(self, A, B, C):
        '''
        Compare the powers of two integers A and B raised to the exponent C.
        Returns a string indicating which power is greater or if they are equal.
        '''
        result_A = custom_pow(A, C)
        result_B = custom_pow(B, C)
        if result_A > result_B:
            return "A is greater"
        elif result_A < result_B:
            return "B is greater"
        else:
            return "A and B are equal"