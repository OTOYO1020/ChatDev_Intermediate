'''
Module containing the function to check if heights can be made non-decreasing.
'''
from typing import List
def canBeNonDecreasing(N: int, H: List[int]) -> bool:
    # If there is only one height, it is trivially non-decreasing
    if N == 1:
        return True
    # Iterate through the heights starting from the second element
    for i in range(1, N):
        # Check if the current height is less than the previous height
        if H[i] < H[i - 1]:
            # If H[i] + 1 is less than H[i-1], we cannot adjust H[i] to meet H[i-1]
            if H[i] + 1 < H[i - 1]:
                return False  # Cannot adjust H[i] to meet H[i-1]
    # If we complete the loop without returning False, it's possible to make heights non-decreasing
    return True