'''
Grid class to manage the grid operations and connectivity checks.
'''
class Grid:
    def __init__(self, n, grid_input):
        self.n = n
        self.grid = [list(row) for row in grid_input]
    def get_white_squares(self):
        '''Returns a list of coordinates of all white squares ('.') in the grid.'''
        return [(i, j) for i in range(self.n) for j in range(self.n) if self.grid[i][j] == '.']
    def is_connected(self, squares):
        '''Checks if the given squares form a connected component using BFS.'''
        if not squares:  # Check for empty squares
            return False
        visited = set()
        queue = [squares[0]]  # Start from the first square in the combination
        while queue:
            square = queue.pop(0)
            if square not in visited:
                visited.add(square)
                for neighbor in self.get_neighbors(square):
                    if neighbor in squares and neighbor not in visited:
                        queue.append(neighbor)
        # Ensure that all squares in the combination are visited
        return len(visited) == len(squares)
    def get_neighbors(self, square):
        '''Returns the valid neighbors of a given square that are white squares.'''
        x, y = square
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n and self.grid[nx][ny] == '.':
                neighbors.append((nx, ny))
        return neighbors