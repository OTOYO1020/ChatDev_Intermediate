'''
Grid class to manage the grid, reachability, and operations calculation.
'''
import math
from collections import deque
class Grid:
    def __init__(self, size, distance_squared):
        self.size = size + 1  # Adjust for 1-based indexing
        self.distance_squared = distance_squared
        self.reachable = [[False] * self.size for _ in range(self.size)]
        self.min_operations = [[float('inf')] * self.size for _ in range(self.size)]
        self.calculate_reachability()
    def calculate_reachability(self):
        # Calculate the maximum distance d
        d = int(math.sqrt(self.distance_squared))
        dx_dy_pairs = []
        # Find all (dx, dy) pairs such that dx^2 + dy^2 = M
        for dx in range(-d, d + 1):
            for dy in range(-d, d + 1):
                if dx * dx + dy * dy == self.distance_squared:
                    dx_dy_pairs.append((dx, dy))
        self.bfs(dx_dy_pairs)  # Pass the list of pairs to BFS
    def bfs(self, dx_dy_pairs):
        # Start BFS from (1, 1) for 1-based indexing
        queue = deque([(1, 1, 0)])  # Starting position is (1, 1)
        self.reachable[1][1] = True  # Mark starting position as reachable
        self.min_operations[1][1] = 0  # Starting position has 0 operations
        while queue:
            x, y, ops = queue.popleft()
            for dx, dy in dx_dy_pairs:
                nx, ny = x + dx, y + dy
                # Check if the new position is within bounds (1-based)
                if 1 <= nx < self.size and 1 <= ny < self.size:  
                    if not self.reachable[nx][ny]:  # If not already marked as reachable
                        self.reachable[nx][ny] = True
                        self.min_operations[nx][ny] = ops + 1
                        queue.append((nx, ny, ops + 1))
    def get_reachable(self):
        return self.reachable
    def get_min_operations(self):
        return self.min_operations