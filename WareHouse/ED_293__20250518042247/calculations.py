'''
Module for calculations related to the geometric series.
'''
from math import gcd  # Import gcd for coprimality check
def modular_exponentiation(base, exp, mod):
    '''
    Efficiently computes (base^exp) % mod using exponentiation by squaring.
    '''
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result
def modular_inverse(a, m):
    '''
    Computes the modular multiplicative inverse of a under modulo m.
    '''
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1
def calculate_sum(A, X, M):
    '''
    Calculates the sum of the geometric series based on the parameters A, X, and M.
    If A = 1, the sum is simply X (the number of terms) modulo M.
    '''
    if A < 1 or M < 1:
        raise ValueError("A and M must be greater than zero.")
    if A == 1:
        # Directly return X modulo M for the case when A = 1
        return X % M  # Correctly return X modulo M as the sum when A = 1
    # Calculate A^X % M using modular exponentiation
    A_mod_M = modular_exponentiation(A, X, M)
    numerator = (A_mod_M - 1 + M) % M
    denominator = (A - 1) % M
    # Check if denominator is zero
    if denominator == 0:
        raise ValueError("Denominator is zero, which is invalid for division.")
    # Check if denominator is coprime to M
    if gcd(denominator, M) != 1:
        raise ValueError("Denominator is not coprime to M, modular inverse cannot be computed.")
    denominator_inv = modular_inverse(denominator, M)
    return (numerator * denominator_inv) % M