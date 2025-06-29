'''
Grid class to manage the illumination logic and grid representation.
'''
from typing import List, Tuple
class Grid:
    def __init__(self, height: int, width: int, bulbs: List[Tuple[int, int]], blocks: List[Tuple[int, int]]):
        self.height = height
        self.width = width
        self.bulbs = bulbs
        self.blocks = blocks
        self.grid = [['empty' for _ in range(width)] for _ in range(height)]
        self.setup_grid()
    def setup_grid(self):
        # Check for overlapping bulbs and blocks
        for bulb in self.bulbs:
            if bulb in self.blocks:
                raise ValueError(f"Error: Bulb and Block cannot overlap at position ({bulb[0]+1}, {bulb[1]+1}).")
        # Mark the positions of blocks in the grid
        for block in self.blocks:
            x, y = block
            self.grid[x][y] = 'block'
        # Then mark the positions of bulbs in the grid
        for bulb in self.bulbs:
            x, y = bulb
            self.grid[x][y] = 'bulb'
    def count_illuminated_squares(self) -> int:
        # Return 0 if there are no bulbs
        if not self.bulbs:
            return 0
        illuminated = set()
        for bulb in self.bulbs:
            self.illuminate(bulb[0], bulb[1], illuminated)
        return len(illuminated)
    def illuminate(self, x: int, y: int, illuminated: set):
        # Add the bulb's own position to the illuminated set
        illuminated.add((x, y))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        # Illuminate in all four directions
        for dx, dy in directions:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                # Check for out-of-bounds and block
                if not (0 <= nx < self.height and 0 <= ny < self.width):
                    break  # Stop if out of bounds
                if self.grid[nx][ny] == 'block':
                    break  # Stop if a block is encountered
                # Check if the next square is adjacent to a block
                if (nx, ny) in self.blocks:
                    break  # Stop if a block is adjacent
                illuminated.add((nx, ny))  # Mark the square as illuminated
    def draw_grid(self):
        # Print the grid representation for debugging purposes
        for row in self.grid:
            print(' '.join(row))