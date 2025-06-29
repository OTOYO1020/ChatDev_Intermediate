'''
Module for processing the grid and calculating humidified cells.
'''
class GridProcessor:
    def __init__(self, grid, D):
        self.grid = grid
        self.D = D
    def get_floor_cells(self):
        '''
        Retrieve the coordinates of all floor cells (cells with '.').
        '''
        floor_cells = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == '.':
                    floor_cells.append((i, j))
        return floor_cells
    def max_humidified(self):
        '''
        Calculate the maximum number of humidified cells based on the positions of two humidifiers.
        '''
        floor_cells = self.get_floor_cells()
        if len(floor_cells) < 2:
            raise ValueError("Not enough floor cells to place two humidifiers. Found only {} floor cells.".format(len(floor_cells)))
        max_humidified = 0
        for i in range(len(floor_cells)):
            for j in range(i + 1, len(floor_cells)):
                humidified_cells = set()
                x1, y1 = floor_cells[i]
                x2, y2 = floor_cells[j]
                for x, y in floor_cells:
                    if abs(x - x1) + abs(y - y1) <= self.D or abs(x - x2) + abs(y - y2) <= self.D:
                        humidified_cells.add((x, y))
                max_humidified = max(max_humidified, len(humidified_cells))
        return max_humidified