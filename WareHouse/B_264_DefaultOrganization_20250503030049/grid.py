'''
Module defining the Grid class for cell color determination.
'''
class Grid:
    def __init__(self):
        self.colors = self.create_grid()
    def create_grid(self):
        """Create a 15x15 grid with colors based on row and column indices."""
        color_names = [
            "red", "green", "blue", "yellow", "cyan", "magenta", "black", 
            "white", "orange", "purple", "pink", "brown", "gray", 
            "lightblue", "lightgreen", "lightgray", "violet", "gold", "navy",
            "teal", "lavender", "coral", "peach", "beige", "turquoise"
        ]
        # Ensure that the color_names list has at least 15 colors
        if len(color_names) < 15:
            raise ValueError("Insufficient colors defined for the grid.")
        return [[color_names[(row + col) % len(color_names)] for col in range(15)] for row in range(15)]
    def get_color(self, row, col):
        """Get the color of the cell at the specified row and column."""
        if 0 <= row < 15 and 0 <= col < 15:  # Ensure indices are within bounds
            return self.colors[row][col]
        else:
            raise IndexError("Row and Column indices must be within the range of 0 to 14.")