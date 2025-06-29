'''
Main entry point for the Ice Square Game application.
'''
from typing import List, Tuple  # Importing necessary types
from game_logic import count_ice_squares
if __name__ == "__main__":
    N = 5  # Number of rows
    M = 5  # Number of columns
    grid = [
        "RRRRR",
        "RIIII",
        "RIIII",
        "RIRRR",
        "RRRRR"
    ]
    result = count_ice_squares(N, M, grid)  # Removed starting_position parameter
    print(f"Total unique ice squares touched: {result}")