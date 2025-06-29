'''
Module to calculate the maximum total comfort for players.
'''
from typing import List
from itertools import permutations
class ComfortCalculator:
    def max_total_comfort(self, N: int, A: List[int]) -> int:
        if N <= 0:
            return 0
        if N == 1:
            return 0  # Only one player, comfort is 0
        max_comfort = 0
        # Evaluate all permutations of player arrivals
        for order in permutations(range(N)):
            comfort = 0
            current_circle = []
            for idx, i in enumerate(order):
                if idx == 0:
                    # First player arrives, comfort is 0
                    current_circle.append(i)
                    continue
                # Calculate comfort for the current player based on the current circle
                left = current_circle[-1]  # Last player in the circle
                right = current_circle[0] if len(current_circle) > 1 else -1  # First player if circle has more than one
                # Calculate comfort for the current player
                if len(current_circle) > 1:  # More than one player in the circle
                    comfort += A[left] + A[right]
                else:  # Only one player in the circle
                    comfort += A[left]  # Only left player (the first one)
                current_circle.append(i)  # Add the current player to the circle
            max_comfort = max(max_comfort, comfort)
        return max_comfort