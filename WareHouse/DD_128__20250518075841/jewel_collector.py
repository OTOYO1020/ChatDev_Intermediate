'''
This module defines the function to calculate the maximum jewel sum based on operations.
'''
from collections import deque
from typing import List
def max_jewel_sum(N: int, K: int, V: List[int], operations: List[str]) -> int:
    D = deque(V)  # Initialize deque with jewel values
    hand = []     # List to hold jewels collected
    max_sum = 0   # Variable to track the maximum sum of jewels collected
    # Adjust K if it exceeds the number of jewels
    K = min(K, N)
    for i in range(K):  # Ensure we do not exceed the number of operations
        operation = operations[i]
        if operation == 'A' and D:
            hand.append(D.popleft())  # Take the leftmost jewel
        elif operation == 'B' and D:
            hand.append(D.pop())      # Take the rightmost jewel
        elif operation == 'C' and hand:
            D.appendleft(hand.pop())  # Move a jewel from hand to the left end of D
        elif operation == 'D' and hand:
            D.append(hand.pop())      # Move a jewel from hand to the right end of D
        # No need for an else statement; simply skip invalid operations
        current_sum = sum(hand)      # Calculate the current sum of jewels in hand
        if current_sum > max_sum:    # Update max_sum if current_sum is greater
            max_sum = current_sum
    return max_sum