'''
Utility class for generating a grid based on specified parameters.
'''
class GridGenerator:
    def __init__(self, N, A, B):
        '''
        Initializes the GridGenerator with specified parameters.
        Parameters:
        N (int): The number of tiles in each dimension.
        A (int): The height of each tile.
        B (int): The width of each tile.
        '''
        self.N = N
        self.A = A
        self.B = B
    def create_grid(self):
        '''
        Creates a grid based on the specified parameters.
        Returns:
        list: A 2D list representing the generated grid.
        '''
        # Initialize the grid with the correct dimensions
        grid = [[' ' for _ in range(self.B * self.N)] for _ in range(self.A * self.N)]
        for i in range(1, self.N + 1):
            for j in range(1, self.N + 1):
                # Determine the color of the tile
                color = 'B' if (i + j) % 2 != 0 else 'W'  # Use 'B' for black and 'W' for white
                for r in range(self.A):
                    for c in range(self.B):
                        grid[(i - 1) * self.A + r][(j - 1) * self.B + c] = color
        return grid