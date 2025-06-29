'''
This file contains the HitAndBlowGame class.
'''
import random
class HitAndBlowGame:
    def __init__(self):
        self.generated_number = self.generate_number()
        self.remaining_lives = 7
    def generate_number(self):
        digits = random.sample(range(0, 10), 3)
        return ''.join(map(str, digits))
    def validate_input(self, number):
        if not number.isdigit() or len(number) != 3:
            return False
        if len(set(number)) != 3:
            return False
        return True
    def check_guess(self, guess):
        if not self.validate_input(guess):
            return "Invalid input. Please enter a three-digit number with different digits."
        if guess == self.generated_number:
            return "Congratulations! You guessed the number correctly."
        self.remaining_lives -= 1
        hits = 0
        blows = 0
        for i in range(3):
            if guess[i] == self.generated_number[i]:
                hits += 1
            elif guess[i] in self.generated_number:
                blows += 1
        if hits == 3:
            return "Congratulations! You guessed the number correctly."
        if self.remaining_lives == 3:
            return f"Hits: {hits}, Blows: {blows}, Remaining Lives: {self.remaining_lives}. You're halfway through the game!"
        if self.remaining_lives == 0:
            return f"Game Over. The correct number was {self.generated_number}."
        return f"Hits: {hits}, Blows: {blows}, Remaining Lives: {self.remaining_lives}"