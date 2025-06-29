'''
Module for calculating the maximum product of the largest K integers from a list.
'''
from typing import List
def mod_inverse(x: int, mod: int) -> int:
    # Function to find modular inverse using Fermat's Little Theorem
    return pow(x, mod - 2, mod)
def max_product(N: int, K: int, A: List[int]) -> int:
    MOD = 10**9 + 7
    A.sort(reverse=True)
    if K == N:
        # If K is equal to N, calculate the product of all elements
        product = 1
        for num in A:
            product = (product * num) % MOD
        return product
    product = 1
    negative_count = 0
    positive_count = 0
    largest_negatives = []
    # Calculate the product of the largest K elements
    for i in range(K):
        if A[i] < 0:
            negative_count += 1
            largest_negatives.append(A[i])
        else:
            positive_count += 1
        product = (product * A[i]) % MOD
    # Handle the case where K is odd and there are no positive numbers
    if K % 2 == 1 and positive_count == 0:
        # Select the K largest negative numbers
        if len(largest_negatives) < K:
            return 0  # Not enough negative numbers to choose from
        largest_negatives.sort(reverse=True)  # Sort to get the largest K negatives
        product = 1
        for i in range(K):
            product = (product * largest_negatives[i]) % MOD
        return product
    # If we have an odd number of negatives, we need to adjust the product
    if negative_count % 2 == 1:
        largest_negative = max(largest_negatives)
        # Find the next largest positive number if available
        next_largest_positive = None
        for num in A[K:]:
            if num > 0:
                next_largest_positive = num
                break
        # Adjust the product
        if next_largest_positive is not None:
            product = (product * next_largest_positive) % MOD
        else:
            # If no positive number is available, exclude the largest negative
            product = (product * mod_inverse(largest_negative, MOD)) % MOD
    return product