'''
Utility functions for mathematical operations.
'''
MOD = 10**9 + 7
def mod_inverse(a, p):
    return pow(a, p - 2, p)
# The combinations function is now integrated into DistanceCalculator