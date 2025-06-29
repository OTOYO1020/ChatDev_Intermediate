'''
Module for counting valid key combinations based on test cases.
'''
from typing import List, Tuple
def count_valid_key_combinations(N: int, M: int, K: int, tests: List[Tuple[List[int], str]]) -> int:
    valid_count = 0
    total_combinations = 1 << N  # 2^N combinations
    for combination in range(total_combinations):
        if validate_combination(combination, N, K, tests):
            valid_count += 1
    return valid_count
def validate_combination(combination: int, N: int, K: int, tests: List[Tuple[List[int], str]]) -> bool:
    for keys, result in tests:
        # Validate that all keys are within the valid range and unique
        if len(keys) != len(set(keys)) or any(key < 1 or key > N for key in keys):
            return False  # Invalid key index or duplicate keys
        # Count how many of the specified keys are real in the current combination
        keys_count = sum(1 for i in keys if (combination & (1 << (i - 1))) != 0)
        # Validate against the expected result
        if result == 'o':
            if keys_count < K:  # Ensure at least K real keys
                return False  # Not enough real keys
        elif result == 'x':
            if keys_count >= K:  # Too many real keys
                return False  # Too many real keys
    return True  # All tests passed