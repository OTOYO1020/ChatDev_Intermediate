'''
Module to manage query generation and response processing.
'''
import random
# Constants for sequence states
EVEN = 0
ODD = 1
UNCERTAIN = None
CONFLICT = -1
class QueryManager:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.sequence = [UNCERTAIN] * n  # None for uncertain, 0 for even, 1 for odd
        self.query_count = 0
        self.last_query = []
    def generate_query(self):
        self.query_count += 1
        self.last_query = random.sample(range(1, self.n + 1), self.k)
        return self.last_query
    def process_response(self, response, query):
        for x in query:
            index = x - 1  # Convert to 0-based index
            if response == 0:  # Even sum
                if self.sequence[index] is UNCERTAIN:
                    self.sequence[index] = EVEN
                elif self.sequence[index] == ODD:
                    self.resolve_conflict(index, EVEN)
            elif response == 1:  # Odd sum
                if self.sequence[index] is UNCERTAIN:
                    self.sequence[index] = ODD
                elif self.sequence[index] == EVEN:
                    self.resolve_conflict(index, ODD)
    def resolve_conflict(self, index, new_value):
        # Logic to resolve conflicts
        # Here we can implement a simple majority rule or keep track of counts
        # For simplicity, we will just overwrite the value for now
        self.sequence[index] = new_value
    def is_sequence_determined(self):
        return all(x is not CONFLICT for x in self.sequence) and all(x is not UNCERTAIN for x in self.sequence)
    def get_sequence(self):
        if CONFLICT in self.sequence:
            raise ValueError("The sequence contains conflicts and cannot be determined.")
        return self.sequence