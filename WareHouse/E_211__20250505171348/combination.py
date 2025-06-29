'''
Module to handle combinations of white squares and check connectivity.
'''
from itertools import combinations
class Combination:
    def __init__(self, grid):
        self.grid = grid
    def is_connected(self, selected_squares):
        '''
        Check if the selected squares are connected using DFS.
        '''
        if not selected_squares:
            return False
        if len(selected_squares) == 1:
            return True  # A single square is connected to itself
        visited = set()
        stack = [selected_squares[0]]  # Start DFS from the first square
        while stack:
            square = stack.pop()
            if square not in visited:
                visited.add(square)
                neighbors = self.get_neighbors(square)
                for neighbor in neighbors:
                    if neighbor in selected_squares and neighbor not in visited:
                        stack.append(neighbor)
        # Check if all selected squares were visited
        return len(visited) == len(selected_squares)
    def get_neighbors(self, square):
        '''
        Get valid neighbors of a square that are white squares, including diagonal neighbors.
        '''
        x, y = square
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.grid.size and 0 <= ny < self.grid.size:
                if (nx, ny) in self.grid.white_squares:  # Check if the neighbor is a white square
                    neighbors.append((nx, ny))
        return neighbors
    def count_valid_combinations(self, K):
        '''
        Count the number of valid combinations of K connected white squares.
        '''
        valid_count = 0
        for selected in combinations(self.grid.white_squares, K):
            if self.is_connected(selected):
                valid_count += 1
        return valid_count