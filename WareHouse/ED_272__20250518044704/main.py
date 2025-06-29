'''
Main file to execute the program and run test cases.
'''
from typing import List
from logic import find_minimum_excluded_integer
def test_find_minimum_excluded_integer():
    assert find_minimum_excluded_integer(5, 3, [0, 1, 2, 3, 4]) == 5  # After 3 iterations, 5 is the first excluded integer
    assert find_minimum_excluded_integer(5, 1, [0, 1, 2, 3, 4]) == 0  # After 1 iteration, 0 is excluded
    assert find_minimum_excluded_integer(5, 5, [0, 1, 2, 3, 4]) == 30  # After 5 iterations, 30 is the first excluded integer
    assert find_minimum_excluded_integer(3, 2, [1, 2, 3]) == 0  # 0 is excluded
    assert find_minimum_excluded_integer(0, 0, []) == 0  # Edge case with empty list
    assert find_minimum_excluded_integer(5, 0, [0, 1, 2, 3, 4]) == 5  # No operations, 5 is excluded
    assert find_minimum_excluded_integer(5, 10, [0, 0, 0, 0, 0]) == 15  # All zeros, after 10 iterations, 15 is excluded
    print("All test cases passed.")
if __name__ == "__main__":
    test_find_minimum_excluded_integer()