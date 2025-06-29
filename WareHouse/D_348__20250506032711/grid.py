'''
Module to handle grid representation and operations.
'''
class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.start = None
        self.goal = None
        self.grid = []
    def read_grid(self):
        for _ in range(self.height):
            row = input().strip()
            self.grid.append(row)
            if 'S' in row:
                self.start = (len(self.grid) - 1, row.index('S'))
            if 'T' in row:
                self.goal = (len(self.grid) - 1, row.index('T'))
    def find_positions(self):
        return self.start, self.goal