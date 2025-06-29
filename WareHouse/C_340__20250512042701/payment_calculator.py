'''
Module for calculating the total payment based on the integer N.
'''
from collections import deque  # Import deque for efficient operations
def calculate_total_payment(N: int) -> int:
    total_payment = 0
    blackboard = deque([N])  # Use a deque for the blackboard
    # Loop until there are no integers >= 2 on the blackboard
    while any(x >= 2 for x in blackboard):  # Continue until all integers are less than 2
        x = blackboard.popleft()  # Get the first integer from the blackboard
        if x >= 2:
            total_payment += x  # Add x to total payment
            # Calculate new integers to be added to the blackboard
            floor_x = x // 2
            ceil_x = (x + 1) // 2
            # Add the new integers to the blackboard
            blackboard.extend([floor_x, ceil_x])
    return total_payment