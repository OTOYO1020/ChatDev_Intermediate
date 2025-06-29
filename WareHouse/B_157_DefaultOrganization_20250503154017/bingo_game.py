'''
This module contains the BingoGame class which handles the logic of the bingo game.
'''
class BingoGame:
    def __init__(self, card, chosen_numbers):
        self.card = card
        self.chosen_numbers = set(chosen_numbers)  # Ensure chosen numbers are unique
        self.marked_numbers = set()
    def mark_numbers(self):
        for row in self.card:
            for number in row:
                if number in self.chosen_numbers:
                    self.marked_numbers.add(number)
    def check_bingo(self):
        # Check rows
        for row in self.card:
            if len(set(row) & self.marked_numbers) == 3:
                return True
        # Check columns
        for col in range(3):
            if len({self.card[row][col] for row in range(3)} & self.marked_numbers) == 3:
                return True
        # Check diagonals
        if len({self.card[i][i] for i in range(3)} & self.marked_numbers) == 3:
            return True
        if len({self.card[i][2 - i] for i in range(3)} & self.marked_numbers) == 3:
            return True
        return False