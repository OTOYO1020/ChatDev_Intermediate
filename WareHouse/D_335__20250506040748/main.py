'''
Main application file for the Takahashi and Dragon Parts placement.
'''
from grid import Grid  # Importing the Grid class
class MainApp:
    def __init__(self):
        self.grid = None
        self.create_input_dialog()
    def create_input_dialog(self):
        n = self.get_input()
        if n is not None:
            self.create_grid(n)
            self.draw_grid()
    def get_input(self):
        while True:
            try:
                n = int(input("Enter an odd number between 3 and 45: "))
                if n < 3 or n > 45 or n % 2 == 0:
                    print("Please enter a valid odd number between 3 and 45.")
                else:
                    return n
            except ValueError:
                print("Invalid input. Please enter a number.")
    def create_grid(self, n):
        self.grid = Grid(n)
        self.grid.place_parts()
    def draw_grid(self):
        for row in self.grid.get_grid():
            print(" ".join(f"{cell:2}" for cell in row))  # Format output for better readability
if __name__ == "__main__":
    app = MainApp()