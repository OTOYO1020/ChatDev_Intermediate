'''
Module for handling grid input and validation.
'''
from typing import List, Tuple
class GridInput:
    def __init__(self, grid_data: List[str], medicines_data: List[str]):
        self.grid_data = grid_data
        self.medicines_data = medicines_data
        self.start = None
        self.goal = None
        self.grid = self.get_grid()  # Initialize grid and find start/goal
    def get_grid(self) -> List[List[str]]:
        grid = []
        for r, line in enumerate(self.grid_data):
            row = list(line.strip())
            if 'S' in row:
                self.start = (r, row.index('S'))  # Store start position
            if 'T' in row:
                self.goal = (r, row.index('T'))  # Store goal position
            grid.append(row)
        if self.start is None or self.goal is None:
            return None  # Invalid grid input
        return grid
    def get_medicines(self) -> List[Tuple[int, int, int]]:
        medicines = []
        for medicine in self.medicines_data:
            try:
                r, c, e = map(int, medicine.split(','))
                medicines.append((r, c, e))
            except ValueError:
                continue  # Ignore invalid entries
        return medicines
    def get_start(self) -> Tuple[int, int]:
        return self.start
    def get_goal(self) -> Tuple[int, int]:
        return self.goal