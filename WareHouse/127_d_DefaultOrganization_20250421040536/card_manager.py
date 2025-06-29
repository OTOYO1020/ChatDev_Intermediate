'''
Contains the CardManager class for managing card values and operations.
'''
import heapq
class CardManager:
    def __init__(self, n, a):
        self.n = n
        self.cards = a
    def apply_operations(self, operations):
        # Organizing and preparing operations
        operations.sort(key=lambda x: x[1], reverse=True)  # Sort by C_j descending
        # Create a min-heap from the current card values
        heapq.heapify(self.cards)
        for b, c in operations:
            # Optimal card rewriting
            count = 0  # Count how many cards we have replaced
            # Determine the actual number of cards to replace
            while count < b and self.cards and self.cards[0] < c:
                smallest_card = heapq.heappop(self.cards)  # Remove the smallest card
                heapq.heappush(self.cards, c)  # Add the new value c to the heap
                count += 1  # Increment the count of replaced cards
        # Ensure that we return the sum of the modified cards
        return self.get_max_sum()
    def get_max_sum(self):
        # Calculate the sum of the cards after applying operations
        return sum(self.cards)  # This will return the sum of the remaining cards