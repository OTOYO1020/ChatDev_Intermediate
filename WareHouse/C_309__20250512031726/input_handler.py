'''
Handles user input and validates it.
'''
from typing import List, Tuple
class InputHandler:
    def __init__(self, n: int, k: int, days: List[Tuple[int, int]]):
        self.n = n
        self.k = k
        self.days = days
    def validate_input(self) -> bool:
        if not (1 <= self.n <= 100) or not (0 <= self.k <= 1000):
            return False
        for a, b in self.days:
            if not (1 <= a <= 100) or not (1 <= b <= 100):
                return False
        return True