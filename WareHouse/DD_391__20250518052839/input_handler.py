'''
Handles user input and validation for the application.
'''
from typing import List, Tuple
class InputHandler:
    @staticmethod
    def get_input(N: int, W: int, blocks: List[Tuple[int, int]], Q: int, queries: List[Tuple[int, int]]) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
        # Validate and process input
        if N <= 0 or W <= 0 or Q < 0:
            raise ValueError("Invalid input values.")
        for x, y in blocks:
            if not (0 <= x < W and 0 <= y < N):
                raise ValueError(f"Block position ({x}, {y}) is out of bounds.")
        for index, time in queries:
            if not (0 <= index < len(blocks)):
                raise ValueError(f"Query index {index} is out of bounds.")
            if time < 0:
                raise ValueError(f"Query time {time} cannot be negative.")
        return blocks, queries
    @staticmethod
    def display_error(message: str):
        print(f"Input Error: {message}")  # Changed to print for standard output