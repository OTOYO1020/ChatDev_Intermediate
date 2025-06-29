'''
Main application file for the GCD calculation.
'''
from gcd_utils import gcd_of_list
import math
from itertools import combinations
def calculate_max_gcd(N, K, A):
    max_gcd = 0
    if K > N:
        raise ValueError("K cannot be greater than N.")  # Raise an exception for invalid input
    if K == 1:  # Directly return the maximum element for K = 1
        return max(A)
    if K == N:  # If K equals N, compute GCD of the entire list
        return gcd_of_list(A)
    for i in range(N):
        # Create a subset that includes A[i] and K-1 other elements from A
        for other_elements in combinations(A, K-1):
            if A[i] in other_elements:  # Ensure A[i] is included in the combination
                chosen_elements = [A[i]] + list(other_elements)
                current_gcd = gcd_of_list(chosen_elements)  # Calculate GCD of the chosen elements
                max_gcd = max(max_gcd, current_gcd)
    return max_gcd
if __name__ == "__main__":
    try:
        N = int(input("Enter N (length of sequence A): "))
        K = int(input("Enter K (number of elements in subset, must be positive): "))
        if K <= 0:
            raise ValueError("K must be a positive integer.")  # Ensure K is positive
        A = list(map(int, input("Enter sequence A (space-separated integers): ").split()))
        if len(A) != N:
            raise ValueError("Length of sequence A must be equal to N.")
        max_gcd = calculate_max_gcd(N, K, A)
        print(f"Maximum GCD: {max_gcd}")
    except ValueError as e:
        print(f"Input Error: {e}")