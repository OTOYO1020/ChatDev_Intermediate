'''
Module for managing the grid and painting operations.
'''
from typing import Dict, List, Tuple
class GridPainter:
    def __init__(self, H: int, W: int):
        self.H = H
        self.W = W
        self.grid = [[0 for _ in range(W)] for _ in range(H)]
        self.color_count = {}  # Initialize color count dictionary
    def apply_paint(self, operations: List[Tuple[int, int, int]]):
        # Create a grid to store the final colors
        self.grid = [[0 for _ in range(self.W)] for _ in range(self.H)]
        self.color_count = {}  # Reset color count dictionary
        # Iterate through operations in the original order
        for operation in operations:
            T_i, A_i, color = operation
            if T_i == 1:  # Paint row
                for col in range(self.W):
                    old_color = self.grid[A_i][col]
                    if old_color != color:  # Only update if the color is changing
                        if old_color != 0:
                            self.color_count[old_color] -= 1
                            if self.color_count[old_color] == 0:
                                del self.color_count[old_color]
                        self.grid[A_i][col] = color
                        self.color_count[color] = self.color_count.get(color, 0) + 1
            elif T_i == 2:  # Paint column
                for row in range(self.H):
                    old_color = self.grid[row][A_i]
                    if old_color != color:  # Only update if the color is changing
                        if old_color != 0:
                            self.color_count[old_color] -= 1
                            if self.color_count[old_color] == 0:
                                del self.color_count[old_color]
                        self.grid[row][A_i] = color
                        self.color_count[color] = self.color_count.get(color, 0) + 1
    def count_colors(self) -> Dict[int, int]:
        return self.color_count  # Return the color counts directly
def paint_grid(H: int, W: int, M: int, operations: List[Tuple[int, int, int]]) -> Dict[int, int]:
    grid_painter = GridPainter(H, W)  # Initialize the grid painter with dimensions H x W
    grid_painter.apply_paint(operations)  # Pass operations to apply_paint
    return grid_painter.count_colors()  # Return the color counts