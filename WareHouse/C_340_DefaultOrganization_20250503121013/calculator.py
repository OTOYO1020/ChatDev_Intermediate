'''
Module for calculating the total cost incurred by Takahashi.
'''
import heapq
def calculate_total_cost(n):
    total_cost = 0
    blackboard = []
    # Initialize the blackboard with the input integer
    heapq.heappush(blackboard, -n)  # Use a max-heap by pushing negative values
    while blackboard and -blackboard[0] >= 2:
        x = -heapq.heappop(blackboard)  # Get the largest integer
        total_cost += x
        # Calculate floor and ceil of x / 2
        floor_half = x // 2
        ceil_half = (x + 1) // 2
        # Add the new integers back to the blackboard
        heapq.heappush(blackboard, -floor_half)
        heapq.heappush(blackboard, -ceil_half)
    return total_cost