'''
Contains the Game class that manages the game logic.
'''
import random
class Game:
    def __init__(self, N):
        self.N = N
        self.declared_numbers = set()
        self.range_limit = 2 * N + 1
        self.available_numbers = list(range(1, self.range_limit + 1))
    def declare_number(self):
        # Filter available numbers based on declared numbers
        self.available_numbers = [num for num in self.available_numbers if num not in self.declared_numbers]
        if self.available_numbers:
            return random.choice(self.available_numbers)
        else:
            raise Exception("No available numbers to declare.")
    def add_declared_number(self, number):
        self.declared_numbers.add(number)
    def is_game_over(self, aoki_declaration):
        return aoki_declaration == 0