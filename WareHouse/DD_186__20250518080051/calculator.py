'''
Contains the function to calculate the sum of absolute differences between pairs of integers.
'''
from typing import List
def calculate_sum_of_absolute_differences(N: int, A: List[int]) -> int:
    if not (2 <= N <= 200000):
        raise ValueError("N must be between 2 and 200,000.")
    if any(not (-100000000 <= x <= 100000000) for x in A):
        raise ValueError("Each integer A_i must be within the range of -100,000,000 to 100,000,000.")
    A.sort()  # Sort the array to facilitate the calculation of absolute differences
    total_sum = 0
    prefix_sum = 0  # To keep track of the sum of elements before the current index
    for i in range(N):
        # Each A[i] contributes to the total sum based on its position in the sorted array
        total_sum += A[i] * i - prefix_sum
        prefix_sum += A[i]  # Update the prefix sum with the current element
    return total_sum
def test_calculate_sum_of_absolute_differences():
    assert calculate_sum_of_absolute_differences(2, [1, 2]) == 1
    assert calculate_sum_of_absolute_differences(3, [1, 2, 3]) == 4
    assert calculate_sum_of_absolute_differences(4, [1, 1, 1, 1]) == 0
    assert calculate_sum_of_absolute_differences(5, [-1, 0, 1, 2, 3]) == 20
    assert calculate_sum_of_absolute_differences(5, [1, 100000000, -100000000, 0, 50000]) == 400000000
    print("All tests passed!")
# Uncomment the following line to run tests when this module is executed
# test_calculate_sum_of_absolute_differences()