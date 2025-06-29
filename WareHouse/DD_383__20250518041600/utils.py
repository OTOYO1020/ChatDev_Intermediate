'''
Utility functions for calculating numbers with exactly 9 divisors and prime number generation.
'''
import math
def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def sieve_of_eratosthenes(limit: int) -> list:
    """Generate a list of prime numbers up to a given limit using the Sieve of Eratosthenes algorithm."""
    primes = []
    is_prime = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
    return primes
def count_numbers_with_n_divisors(N: int, d: int) -> int:
    """Count the number of positive integers not greater than N that have exactly d divisors."""
    count = 0
    # Count numbers of the form p^8
    primes = sieve_of_eratosthenes(int(N**(1/8)))  # Limit for p^8
    for p in primes:
        if p ** 8 <= N:
            count += 1
        else:
            break  # No need to check further if p^8 exceeds N
    # Count numbers of the form p^2 * q^2
    primes_for_p2q2 = sieve_of_eratosthenes(int(N**(1/2)))  # Limit for p^2 * q^2
    for i in range(len(primes_for_p2q2)):
        for j in range(i + 1, len(primes_for_p2q2)):  # Ensure j > i to maintain distinct primes
            p2q2 = primes_for_p2q2[i]**2 * primes_for_p2q2[j]**2
            if p2q2 <= N:
                count += 1
            else:
                break  # No need to check further if p^2 * q^2 exceeds N
    return count