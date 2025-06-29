'''
Module for generating combinations and validating test results.
'''
from itertools import product
def generate_combinations(N: int, M: int, K: int, tests: list) -> int:
    '''
    Generate all possible combinations of keys and validate them against test results.
    Parameters:
    N (int): Total number of keys.
    M (int): Number of tests.
    K (int): Minimum number of real keys required for a positive result.
    tests (list): List of tuples containing test data.
    Returns:
    int: Count of valid combinations that satisfy all test results.
    '''
    if not tests:  # Handle empty tests
        return 0
    valid_count = 0
    all_combinations = product([0, 1], repeat=N)  # 0 for dummy, 1 for real
    for combination in all_combinations:
        valid = True
        for C, keys, result in tests:
            real_count = sum(combination[key] for key in keys)  # Count real keys in the current combination
            # Check the result conditions
            if result == 'o' and real_count < K:
                valid = False
                break
            if result == 'x' and real_count >= K:
                valid = False
                break
        if valid:
            valid_count += 1
    return valid_count