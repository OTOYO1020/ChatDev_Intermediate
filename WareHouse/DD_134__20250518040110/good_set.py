'''
Module containing the logic to determine if a good set of choices exists.
'''
from typing import List
def is_good_set(N: int, a: List[int]) -> List[int]:
    choices = [0] * N  # Initialize choices with 0s
    # Iterate through each integer i from 1 to N
    for i in range(1, N + 1):
        total = sum(choices[j - 1] for j in range(i, N + 1, i))  # Calculate current total for multiples of i
        # Check if the current total matches the required parity
        if total % 2 != a[i - 1]:  
            count_needed = (a[i - 1] - total % 2 + 2) % 2  # Determine how many adjustments are needed (0 or 1)
            adjusted = 0
            for j in range(i, N + 1, i):  # Iterate through all multiples of i
                if adjusted < count_needed and choices[j - 1] == 0:  # Find the first multiple that is still 0
                    choices[j - 1] = 1  # Set it to 1
                    adjusted += 1
            if adjusted < count_needed:  # If not enough adjustments could be made, return None
                return None
    return choices  # Return the valid choices if all conditions are satisfied