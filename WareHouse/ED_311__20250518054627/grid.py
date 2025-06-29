'''
Module to handle grid-related operations, including marking holed squares and counting holeless squares.
'''
from typing import List, Tuple
class Grid:
    def __init__(self, height: int, width: int, holed_squares: List[Tuple[int, int]]):
        self.height = height
        self.width = width
        self.holed_squares = holed_squares
        self.grid = [[0] * width for _ in range(height)]
        self.mark_holes()
    def mark_holes(self):
        unique_holes = set(self.holed_squares)  # Convert to a set to remove duplicates
        for x, y in unique_holes:
            if 0 <= x < self.height and 0 <= y < self.width:
                self.grid[x][y] = 1  # Mark as holed
            else:
                print(f"Warning: Holed square coordinates ({x}, {y}) are out of bounds and will be ignored.")
    def count_holeless_squares(self) -> int:
        # Return 0 if there are no holed squares
        if not self.holed_squares:
            return self.height * self.width * (self.height + 1) * (self.width + 1) // 4  # Total squares if no holes
        count = 0
        for i in range(self.height):
            for j in range(self.width):
                max_size = min(self.height - i, self.width - j)
                for size in range(1, max_size + 1):
                    if self.is_holeless(i, j, size):
                        count += 1
                    else:
                        break  # Stop checking larger sizes if a hole is found
        return count
    def is_holeless(self, x: int, y: int, size: int) -> bool:
        for i in range(size):
            for j in range(size):
                if self.grid[x + i][y + j] == 1:
                    return False
        return True