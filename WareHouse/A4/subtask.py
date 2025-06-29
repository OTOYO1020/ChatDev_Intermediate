'''
This file contains the Subtask class.
'''
import random
class Subtask:
    def __init__(self):
        self.target_number = self.generate_target_number()
        self.remaining_lives = 7
    def generate_target_number(self):
        digits = list(range(10))
        random.shuffle(digits)
        return "".join(str(digit) for digit in digits[:3])
    def check_guess(self, guess):
        if len(guess) != 3 or not guess.isdigit():
            return False, "Invalid input. Please enter a three-digit number."
        if len(set(guess)) != 3:
            return False, "Invalid input. Please enter a number with different digits."
        if self.remaining_lives == 0:
            return False, f"Game over. The target number was {self.target_number}."
        if guess == self.target_number:
            self.remaining_lives = 0  # Update remaining lives to 0
            return True, "Congratulations! You guessed the number correctly."
        hits = 0
        blows = 0
        for i in range(3):
            if guess[i] == self.target_number[i]:
                hits += 1
            elif guess[i] in self.target_number:
                blows += 1
        if hits == 3 and blows == 0:
            self.remaining_lives = 0  # Update remaining lives to 0
            return True, "Congratulations! You guessed the number correctly."
        else:
            self.remaining_lives -= 1  # Decrease lives for every valid guess
            return False, f"Hits: {hits}, Blows: {blows}"
    def get_remaining_lives(self):
        return self.remaining_lives
    def is_valid_guess(self, guess):
        if len(guess) != 3 or not guess.isdigit():
            return False
        if len(set(guess)) != 3:
            return False
        return True