'''
Module to handle jewel operations and calculate the maximum sum.
'''
from collections import deque
class JewelsHandler:
    def __init__(self, jewels, max_operations):
        self.jewels = deque(jewels)
        self.max_operations = max_operations
        self.jewels_in_hand = []
        self.max_sum = 0
    def perform_operations(self):
        # Use a queue to explore all states
        queue = deque([(self.jewels.copy(), self.jewels_in_hand.copy(), 0)])  # Ensure a copy of jewels_in_hand
        while queue:
            current_jewels, current_jewels_in_hand, operations_count = queue.popleft()
            # Calculate current sum and update max_sum
            current_sum = sum(current_jewels_in_hand)
            self.max_sum = max(self.max_sum, current_sum)
            if operations_count < self.max_operations:
                # Operation A: Take from left
                if current_jewels:
                    jewel = current_jewels[0]  # Get the leftmost jewel
                    new_jewels = current_jewels.copy()  # Create a new copy for this operation
                    new_jewels.popleft()  # Remove the leftmost jewel
                    new_jewels_in_hand = current_jewels_in_hand + [jewel]
                    queue.append((new_jewels, new_jewels_in_hand, operations_count + 1))
                # Operation B: Take from right
                if current_jewels:
                    jewel = current_jewels[-1]  # Get the rightmost jewel
                    new_jewels = current_jewels.copy()  # Create a new copy for this operation
                    new_jewels.pop()  # Remove the rightmost jewel
                    new_jewels_in_hand = current_jewels_in_hand + [jewel]
                    queue.append((new_jewels, new_jewels_in_hand, operations_count + 1))
                # Operation C: Put back to left
                if current_jewels_in_hand:  # Check if jewels_in_hand is not empty
                    for jewel in current_jewels_in_hand:  # Iterate directly over jewels_in_hand
                        new_jewels = current_jewels.copy()  # Create a new copy for this operation
                        new_jewels.appendleft(jewel)  # Use appendleft for deque
                        new_jewels_in_hand = [j for j in current_jewels_in_hand if j != jewel]  # Remove the jewel from jewels_in_hand
                        queue.append((new_jewels, new_jewels_in_hand, operations_count + 1))
                # Operation D: Put back to right
                if current_jewels_in_hand:  # Check if jewels_in_hand is not empty
                    for jewel in current_jewels_in_hand:  # Iterate directly over jewels_in_hand
                        new_jewels = current_jewels.copy()  # Create a new copy for this operation
                        new_jewels.append(jewel)  # Use append for deque
                        new_jewels_in_hand = [j for j in current_jewels_in_hand if j != jewel]  # Remove the jewel from jewels_in_hand
                        queue.append((new_jewels, new_jewels_in_hand, operations_count + 1))
        return self.max_sum