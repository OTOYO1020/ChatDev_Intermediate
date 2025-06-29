'''
Utility module for calculating the greatest common divisor (gcd).
'''
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a