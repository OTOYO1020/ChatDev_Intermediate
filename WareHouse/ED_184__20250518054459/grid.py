'''
Contains the Grid class and BFS logic for finding the shortest path.
'''
from collections import deque
from typing import List, Tuple
class Grid:
    def __init__(self, H: int, W: int, grid: List[List[str]]):
        self.H = H
        self.W = W
        self.grid = grid
        self.start = self.find_position('S')
        self.goal = self.find_position('G')
    def find_position(self, char: str) -> Tuple[int, int]:
        for i in range(self.H):
            for j in range(self.W):
                if self.grid[i][j] == char:
                    return (i, j)
        return (-1, -1)
    def find_shortest_time(self) -> int:
        if self.start == (-1, -1) or self.goal == (-1, -1):
            return -1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([(self.start[0], self.start[1], 0)])  # (x, y, time)
        visited = set()
        teleport_map = {}
        # Create a teleport map for characters 'a' to 'z'
        for i in range(self.H):
            for j in range(self.W):
                if self.grid[i][j].islower():
                    if self.grid[i][j] not in teleport_map:
                        teleport_map[self.grid[i][j]] = []
                    teleport_map[self.grid[i][j]].append((i, j))
        while queue:
            x, y, time = queue.popleft()
            # Mark current position as visited before exploring neighbors
            visited.add((x, y))
            if (x, y) == self.goal:
                return time
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.H and 0 <= ny < self.W and (nx, ny) not in visited:
                    if self.grid[nx][ny] != '#':
                        queue.append((nx, ny, time + 1))
            # Handle teleportation
            if self.grid[x][y].islower():
                for (tx, ty) in teleport_map[self.grid[x][y]]:
                    if (tx, ty) not in visited:  # Ensure we do not revisit
                        visited.add((tx, ty))  # Mark as visited immediately
                        queue.append((tx, ty, time + 1))  # Add to queue
        return -1