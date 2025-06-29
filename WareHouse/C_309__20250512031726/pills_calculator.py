'''
Implements the logic for calculating the first day with K or fewer pills.
'''
from typing import List, Tuple
class PillsCalculator:
    def __init__(self, n: int, k: int, days: List[Tuple[int, int]]):
        self.n = n
        self.k = k
        self.days = days
    def first_day_with_k_or_less_pills(self) -> int:
        # Calculate the maximum day considering only a_i
        max_day = max((a for a, b in self.days), default=0)
        # Initialize pills_per_day with size max_day + 1 only if max_day > 0
        pills_per_day = [0] * (max_day + 1) if max_day > 0 else []
        # Update pills_per_day for each medicine type
        for a, b in self.days:
            # Ensure we only update valid days
            for day in range(1, a + 1):
                if day < len(pills_per_day):  # Ensure we don't exceed the list bounds
                    pills_per_day[day] += b  # Correctly accumulate pills for each day
        # Find the first day with K or fewer pills
        for day in range(1, max_day + 1):
            if day < len(pills_per_day) and pills_per_day[day] <= self.k:
                return day  # Return the 1-based day number
        return -1  # Return -1 if no day meets the criteria