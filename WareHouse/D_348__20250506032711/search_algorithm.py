'''
Module to implement search algorithms.
'''
from collections import deque
class SearchAlgorithm:
    def __init__(self, grid, medicines):
        self.grid = grid
        self.medicines = medicines
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def bfs(self, initial_energy):
        start = self.grid.start
        goal = self.grid.goal
        queue = deque([(start, initial_energy)])  # (position, current_energy)
        visited = set()
        visited.add(start)
        while queue:
            current, energy = queue.popleft()
            # Check if we reached the goal
            if current == goal and energy > 0:
                return True
            # Explore adjacent cells
            for d in self.directions:
                next_pos = (current[0] + d[0], current[1] + d[1])
                if self.is_valid(next_pos) and next_pos not in visited:
                    visited.add(next_pos)
                    new_energy = energy
                    # If we find a medicine, increase energy
                    if next_pos in self.medicines:
                        new_energy += self.medicines[next_pos].energy
                    # Only add to queue if we have energy to move
                    if new_energy > 0:
                        queue.append((next_pos, new_energy))
            # Check adjacent cells for medicines if energy is zero
            if energy == 0:
                for d in self.directions:
                    adjacent_pos = (current[0] + d[0], current[1] + d[1])
                    if adjacent_pos in self.medicines and adjacent_pos not in visited:
                        new_energy = self.medicines[adjacent_pos].energy
                        visited.add(adjacent_pos)  # Mark as visited
                        queue.append((adjacent_pos, new_energy))  # Move to the medicine position and collect it
                        # Continue searching from the medicine position
                        queue.append((adjacent_pos, new_energy))  # Add the medicine position to the queue
        return False
    def is_valid(self, position):
        row, col = position
        return (0 <= row < self.grid.height and 
                0 <= col < self.grid.width and 
                self.grid.grid[row][col] != '#')