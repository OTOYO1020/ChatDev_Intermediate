'''
Main application file to run the pawn position calculator.
'''
import sys
from pawn_grid import PawnGrid  # Importing the PawnGrid class
from input_handler import InputHandler  # Importing the InputHandler class
class MainApp:
    def __init__(self):
        self.black_pawns = []
    def read_input(self):
        input_handler = InputHandler()
        N, M, black_pawns = input_handler.get_input()
        self.black_pawns = black_pawns
        self.N = N  # Store N as an instance variable
        return N, M
    def calculate_reachable_positions(self, N):
        reachable_count = 0
        for y in range(2 * N + 1):
            if self.is_reachable(y):  # Pass only y to the is_reachable method
                reachable_count += 1
        return reachable_count
    def is_reachable(self, y):
        # Check if the white pawn can reach (2N, Y) based on the movement rules
        pawn_grid = PawnGrid(self.N, self.black_pawns)
        return pawn_grid.is_reachable(y)
    def run(self):
        N, M = self.read_input()
        reachable_count = self.calculate_reachable_positions(N)
        print(f"Reachable Y positions: {reachable_count}")
if __name__ == "__main__":
    app = MainApp()
    app.run()