'''
Calculates the minimum cost to form the target string.
'''
from typing import List
class CostCalculator:
    def min_cost_to_form_string(self, N: int, bags: List[List[str]], T: str) -> int:
        # Initialize a variable to track the minimum cost
        min_cost = [float('inf')] * (len(T) + 1)
        min_cost[0] = 0  # Cost to form an empty string is 0
        # Iterate through each position in the target string
        for i in range(len(T)):
            if min_cost[i] == float('inf'):
                continue  # Skip if this position cannot be formed
            # Iterate through all bags
            for bag in bags:
                for string in bag:
                    # Check if the string can be appended to form T
                    if T.startswith(string, i):
                        next_index = i + len(string)
                        min_cost[next_index] = min(min_cost[next_index], min_cost[i] + 1)
        return min_cost[len(T)] if min_cost[len(T)] != float('inf') else -1