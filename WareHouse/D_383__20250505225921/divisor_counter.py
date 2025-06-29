'''
Module for counting the number of positive divisors of a number and checking for numbers with exactly 9 divisors.
'''
import math
def count_divisors(i):
    '''
    Count the number of positive divisors of the integer i.
    '''
    divisor_count = 0
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0:
            divisor_count += 1  # Count j
            if j != i // j:
                divisor_count += 1  # Count i/j if it's different
    return divisor_count
def sieve_of_eratosthenes(limit):
    '''
    Generate a list of prime numbers up to the specified limit using the Sieve of Eratosthenes.
    '''
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (is_prime[p] == True):
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if is_prime[p]]
def count_numbers_with_nine_divisors(N):
    '''
    Count how many numbers from 1 to N have exactly 9 positive divisors.
    This can happen in three cases:
    1. p^8 (where p is a prime)
    2. p^4 * q (where p and q are distinct primes)
    3. p^2 * q^2 (where p and q are distinct primes)
    '''
    count = 0
    primes = sieve_of_eratosthenes(N)
    seen_numbers = set()  # To avoid counting duplicates
    # Check for p^8
    for p in primes:
        product = p**8
        if product <= N:
            seen_numbers.add(product)
            count += 1
        else:
            break  # No need to check further if p^8 exceeds N
    # Check for p^4 * q
    for i in range(len(primes)):
        p4 = primes[i]**4
        if p4 > N:
            break  # No need to check further if p^4 exceeds N
        for j in range(len(primes)):
            if i != j:  # Ensure p and q are distinct
                product = p4 * primes[j]
                if product <= N:
                    seen_numbers.add(product)
                    count += 1
    # Check for p^2 * q^2
    for i in range(len(primes)):
        p2 = primes[i]**2
        if p2 > N:
            break  # No need to check further if p^2 exceeds N
        for j in range(i + 1, len(primes)):
            product = p2 * primes[j]**2
            if product <= N:
                seen_numbers.add(product)
                count += 1
            else:
                break  # No need to check further if the product exceeds N
    return count