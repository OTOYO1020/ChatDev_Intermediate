'''
Module to handle the application logic.
'''
from grid import Grid
from medicine import Medicine
from search_algorithm import SearchAlgorithm
class App:
    def __init__(self):
        self.grid = None
        self.medicines = {}
    def run(self):
        self.read_input()
        initial_energy = int(input("Enter initial energy level: "))  # Allow user to input initial energy
        search_algorithm = SearchAlgorithm(self.grid, self.medicines)
        if search_algorithm.bfs(initial_energy):
            print("YES")
        else:
            print("NO")
    def read_input(self):
        height, width = map(int, input("Enter grid dimensions (H W): ").split())
        self.grid = Grid(height, width)
        print("Enter the grid representation (use '#' for walls, 'S' for start, 'T' for goal):")
        self.grid.read_grid()
        medicines_data = input("Enter medicines (format: R C E; R C E; ...): ").strip().split(';')
        for data in medicines_data:
            if data:
                r, c, e = map(int, data.split())
                medicine = Medicine(r, c, e)
                self.medicines[medicine.position] = medicine