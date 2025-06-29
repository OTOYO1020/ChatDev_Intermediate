'''
This file contains the HitBlowGame class.
'''
import random
class HitBlowGame:
    def __init__(self):
        self.secret_number = self.generate_secret_number()
        self.remaining_lives = 7
        self.halfway_guessed = False
    def generate_secret_number(self):
        digits = list(range(10))
        random.shuffle(digits)
        return "".join(str(digit) for digit in digits[:3])
    def check_guess(self, guess):
        if not guess.isdigit() or len(guess) != 3:
            return "Invalid input. Please enter a three-digit number."
        if len(set(guess)) != 3 or len(guess) != len(set(guess)):
            return "Invalid input. Please enter a three-digit number with different digits."
        if guess == self.secret_number:
            return "Congratulations! You guessed the number correctly."
        if self.halfway_guessed:
            return "Halfway through. You guessed the number correctly."
        if self.remaining_lives == 0:
            return f"Game Over. The secret number was {self.secret_number}."
        hits = 0
        blows = 0
        secret_digits = list(self.secret_number)
        for i in range(3):
            if guess[i] == secret_digits[i]:
                hits += 1
                secret_digits[i] = None
        for i in range(3):
            if guess[i] in secret_digits and guess[i] != secret_digits[i]:
                blows += 1
                secret_digits[secret_digits.index(guess[i])] = None
        if hits == 3:
            self.halfway_guessed = True
            return "Halfway through. You guessed the number correctly."
        self.remaining_lives -= 1
        return f"Incorrect guess. Hits: {hits}, Blows: {blows}. Remaining lives: {self.remaining_lives}."