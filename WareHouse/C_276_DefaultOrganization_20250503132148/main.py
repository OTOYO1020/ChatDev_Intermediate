'''
Main application file for the permutation generator.
'''
import sys
from utils import generate_permutations, sort_permutations
from math import factorial
def main():
    try:
        # Read input from standard input
        N, K = map(int, input().split())
        # Validate N
        if N < 1:
            print("Error: N must be at least 1.")
            return
        P = list(map(int, input().split()))
        # Validate the length of P
        if len(P) != N:
            print("Error: The length of permutation P must be equal to N.")
            return
        # Validate that P is not the identity permutation
        if P == list(range(1, N + 1)):
            print("Error: Permutation P cannot be the identity permutation.")
            return
        # Validate K
        if K < 1 or K > factorial(N):
            print("Error: K must be at least 1 and less than or equal to the number of permutations.")
            return
        # Generate all permutations
        all_permutations = generate_permutations(N)
        # Sort the permutations
        sorted_permutations = sort_permutations(all_permutations)
        # Get the (K-1)-th permutation
        result_permutation = sorted_permutations[K - 1]
        # Print the result
        print(' '.join(map(str, result_permutation)))
    except ValueError:
        print("Error: Invalid input format. Please enter two integers followed by a permutation.")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()