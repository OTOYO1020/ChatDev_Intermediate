'''
Grid class to manage the grid and its operations.
'''
class Grid:
    def __init__(self):
        self.grid = []
        self.start = None
        self.goal = None
        self.candy_positions = []
    def populate_grid(self, grid_input):
        self.grid = [list(row) for row in grid_input]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 'S':
                    self.start = (i, j)
                elif self.grid[i][j] == 'G':
                    self.goal = (i, j)
                elif self.grid[i][j] == 'o':
                    self.candy_positions.append((i, j))
    def get_candy_positions(self):
        return self.candy_positions