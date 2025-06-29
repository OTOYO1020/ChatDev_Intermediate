'''
Utility functions for checking coprimality.
'''
from math import gcd
from functools import reduce
def is_pairwise_coprime(A):
    '''
    Checks if the integers in the list A are pairwise coprime using a sieve-like approach.
    '''
    max_value = max(A)
    prime_factors = [0] * (max_value + 1)  # Array to track the count of prime factors
    for number in A:
        # Factorize the number
        temp = number
        for factor in range(2, int(temp**0.5) + 1):
            if temp % factor == 0:
                while temp % factor == 0:
                    temp //= factor
                if prime_factors[factor] > 0:
                    return False  # Found a common prime factor
                prime_factors[factor] += 1
        if temp > 1:  # If there's any prime factor left
            if prime_factors[temp] > 0:
                return False  # Found a common prime factor
            prime_factors[temp] += 1
    return True
def gcd_of_list(A):
    '''
    Returns the GCD of the entire list A using an iterative approach.
    '''
    overall_gcd = A[0]
    for number in A[1:]:
        overall_gcd = gcd(overall_gcd, number)
        if overall_gcd == 1:  # Early exit if GCD is 1
            break
    return overall_gcd