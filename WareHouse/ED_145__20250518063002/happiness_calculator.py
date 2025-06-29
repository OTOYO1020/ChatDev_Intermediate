'''
Module for calculating maximum happiness based on eating times and deliciousness values.
'''
from typing import List
class HappinessCalculator:
    def max_happiness(self, N: int, T: int, A: List[int], B: List[int]) -> int:
        # Validate non-negative values
        if N < 0 or len(A) < N or len(B) < N:
            raise ValueError("N must be non-negative and must not exceed the lengths of A and B.")
        if any(a < 0 for a in A):
            raise ValueError("Eating times must be non-negative.")
        if any(b < 0 for b in B):
            raise ValueError("Deliciousness values must be non-negative.")
        if N == 0 or not A or not B:  # Check for no dishes or empty lists
            return 0
        if all(a > T for a in A):  # Check if all dishes exceed the time limit
            return 0
        max_happiness = 0  # Initialize maximum happiness to zero
        # Iterate through each dish to consider it as the first choice
        for i in range(N):
            total_time = A[i]  # Time taken for the first dish
            total_happiness = B[i]  # Happiness from the first dish
            remaining_time = T - total_time  # Calculate remaining time after choosing the first dish
            # If remaining time is negative, skip to the next dish
            if remaining_time < 0:
                continue
            # Create a list of remaining dishes that can be ordered
            remaining_dishes = [(A[j], B[j]) for j in range(N) if j != i and A[j] <= remaining_time]
            remaining_dishes.sort(key=lambda x: x[1], reverse=True)  # Sort remaining dishes by deliciousness in descending order
            # Accumulate happiness from remaining dishes within the remaining time
            for eating_time, deliciousness in remaining_dishes:
                if remaining_time >= eating_time:  # Check if the dish can be ordered within the remaining time
                    total_happiness += deliciousness  # Add the deliciousness to total happiness
                    remaining_time -= eating_time  # Decrease the remaining time
                else:
                    break  # Exit the loop if we can't afford the next dish
            # Update maximum happiness found so far
            max_happiness = max(max_happiness, total_happiness)  # Ensure we consider the happiness from the first dish
        return max_happiness  # Return the maximum happiness value