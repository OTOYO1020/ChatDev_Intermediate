'''
Main application file for generating permutations of a string.
'''
import sys
from permutation_generator import generate_permutations
def main():
    '''
    Main function to read input and generate permutations.
    '''
    # Read input from standard input
    input_data = sys.stdin.read().strip().splitlines()
    if len(input_data) < 2:
        print("Please provide both a string and an integer.")
        return
    S = input_data[0]
    K = input_data[1]
    # Validate the length of S
    if len(S) < 1 or len(S) > 8:
        print("String length must be between 1 and 8 characters.")
        return
    # Validate K
    if not K.isdigit() or int(K) <= 0:
        print("Please enter a valid positive integer for K.")
        return
    K = int(K)  # Convert K to an integer after validation
    # Validate K after conversion
    if K <= 0:
        print("K must be a positive integer.")
        return
    # Generate permutations
    result = generate_permutations(S)
    # Validate K after generating permutations
    if K > len(result):
        print("K is out of range for the number of permutations.")
        return
    print(f"K-th Permutation: {result[K - 1]}")
if __name__ == "__main__":
    main()