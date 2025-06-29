'''
Data processor for calculating generation distances from amoeba data.
'''
from collections import deque
class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.N = len(data)
        self.parent = [0] * (2 * self.N + 2)
        self.generations = [0] * (2 * self.N + 2)
    def calculate_generation_distances(self):
        self.parent[1] = 0  # Amoeba 1 has no parent
        for i in range(1, self.N + 1):
            A_i = self.data[i - 1]
            self.parent[2 * i] = A_i
            self.parent[2 * i + 1] = A_i
        self.generations[1] = 0
        queue = deque([1])  # Using deque for efficient queue operations
        while queue:
            current = queue.popleft()
            for child in (2 * current, 2 * current + 1):
                # Check if child exists, is within the valid range, and has a parent
                if 0 < child < len(self.generations) and self.parent[child] != 0:
                    self.generations[child] = self.generations[current] + 1
                    queue.append(child)
        return self.generations[1:2 * self.N + 2]