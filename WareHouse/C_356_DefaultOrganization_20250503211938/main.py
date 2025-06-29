'''
Main application file for the Test Combination application.
'''
import sys
from itertools import product  # Importing product directly for use in combinations
from combinations import generate_combinations  # Importing the function from combinations module
def main():
    # Read integers N, M, and K from standard input
    N, M, K = map(int, sys.stdin.readline().strip().split())
    # Input validation for N, M, and K
    if N <= 0 or M <= 0 or K < 0:
        raise ValueError("N and M must be positive integers, and K must be a non-negative integer.")
    # Validate M against N
    if M > N:
        raise ValueError(f"The number of tests M cannot exceed the number of keys N. M: {M}, N: {N}")
    tests = []
    # Read each test data
    for _ in range(M):
        C = int(sys.stdin.readline().strip())
        # Validate C
        if C <= 0 or C > N:
            raise ValueError(f"Invalid number of keys: {C}. It must be between 1 and {N}.")
        keys_input = sys.stdin.readline().strip()
        keys = []
        # Validate and parse keys
        for key in keys_input.split():
            key = key.strip()
            if not key.isdigit() or int(key) < 0 or int(key) >= N:
                raise ValueError(f"Invalid key: {key}. Keys must be integers in the range [0, {N-1}].")
            keys.append(int(key))  # Convert to integer here for direct use later
        # Validate the number of keys
        if len(keys) != C:
            raise ValueError(f"Expected {C} keys, but got {len(keys)}. Please check the input.")
        if len(set(keys)) != len(keys):
            raise ValueError("Duplicate keys are not allowed. Please provide unique keys.")
        result = sys.stdin.readline().strip()
        if result not in ('o', 'x'):
            raise ValueError(f"Invalid result: {result}. Result must be either 'o' or 'x'.")
        tests.append((C, keys, result))
    # Generate combinations and count valid ones
    count = generate_combinations(N, M, K, tests)
    print(count)
if __name__ == "__main__":
    main()