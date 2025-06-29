'''
Grid class to manage the grid operations and pathfinding.
'''
from collections import deque
class Grid:
    def __init__(self, height, width, grid_data):
        self.height = height
        self.width = width
        self.grid = grid_data
        self.start = None
        self.goal = None
        self.find_start_and_goal()
        self.mark_line_of_sight()
    def find_start_and_goal(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == 'S':
                    self.start = (i, j)
                elif self.grid[i][j] == 'G':
                    self.goal = (i, j)
    def is_passable(self, x, y):
        return 0 <= x < self.height and 0 <= y < self.width and self.grid[x][y] in ('.', 'S', 'G')
    def mark_line_of_sight(self):
        directions = {'>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] in directions:
                    dx, dy = directions[self.grid[i][j]]
                    x, y = i, j
                    while True:
                        # Check for boundaries before accessing the grid
                        if not (0 <= x + dx < self.height and 0 <= y + dy < self.width):
                            break
                        x += dx
                        y += dy
                        # Stop if we hit another person
                        if self.grid[x][y] in directions:
                            break
                        # Mark as impassable if it's not a person or the start/goal
                        elif self.grid[x][y] not in ('.', 'S', 'G'):
                            self.grid[x][y] = '#'
    def bfs(self):
        queue = deque([(self.start[0], self.start[1], 0)])  # (x, y, moves)
        visited = set()
        visited.add(self.start)
        while queue:
            x, y, moves = queue.popleft()
            if (x, y) == self.goal:
                return moves
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if self.is_passable(nx, ny) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, moves + 1))
        return -1  # Goal is unreachable