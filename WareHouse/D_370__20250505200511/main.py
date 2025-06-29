'''
App class that creates the application for the wall management.
'''
import sys
from grid_manager import GridManager
class App:
    def __init__(self):
        self.grid_manager = self.initialize_grid()
        self.run_application()
    def initialize_grid(self):
        H, W = map(int, input("Please enter grid dimensions (Height Width): ").split())
        return GridManager(H, W)
    def run_application(self):
        Q = int(input("Please enter the number of bomb placement queries: "))
        for _ in range(Q):
            query = input("Please enter bomb coordinates (Row Column): ").split()
            self.grid_manager.process_query(query)
        remaining_walls = self.grid_manager.count_remaining_walls()
        print(f"Total remaining walls: {remaining_walls}")
if __name__ == "__main__":
    App()