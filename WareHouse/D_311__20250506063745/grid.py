'''
Grid class to manage the ice squares and movement logic.
'''
from collections import deque
class Grid:
    def __init__(self, n, m, layout):
        self.n = n
        self.m = m
        self.layout = layout
        self.visited = set()
    def can_move(self, i, j, direction):
        # Check movement in the specified direction and update visited squares
        if direction == 'up':
            while i > 0 and self.layout[i - 1][j] == '.':
                i -= 1
                self.visited.add((i, j))  # Add to visited
            return i > 0 and self.layout[i - 1][j] == '.', (i, j)
        elif direction == 'down':
            while i < self.n - 1 and self.layout[i + 1][j] == '.':
                i += 1
                self.visited.add((i, j))  # Add to visited
            return i < self.n - 1 and self.layout[i + 1][j] == '.', (i, j)
        elif direction == 'left':
            while j > 0 and self.layout[i][j - 1] == '.':
                j -= 1
                self.visited.add((i, j))  # Add to visited
            return j > 0 and self.layout[i][j - 1] == '.', (i, j)
        elif direction == 'right':
            while j < self.m - 1 and self.layout[i][j + 1] == '.':
                j += 1
                self.visited.add((i, j))  # Add to visited
            return j < self.m - 1 and self.layout[i][j + 1] == '.', (i, j)
        return False, (i, j)  # Move not successful
    def explore(self, start_i, start_j):
        # Ensure the starting position is within bounds
        if start_i < 0 or start_i >= self.n or start_j < 0 or start_j >= self.m:
            return 0
        # Check if the starting position is an ice square
        if self.layout[start_i][start_j] != '.':
            return 0
        self.visited.add((start_i, start_j))  # Add starting position if it's an ice square
        directions = ['up', 'down', 'left', 'right']
        # Use a queue to explore all reachable squares
        queue = deque([(start_i, start_j)])
        while queue:
            current_i, current_j = queue.popleft()  # Get the current position
            for direction in directions:
                can_move, (new_i, new_j) = self.can_move(current_i, current_j, direction)
                if can_move and (new_i, new_j) not in self.visited:
                    queue.append((new_i, new_j))  # Add new position to the queue
        return len(self.visited)