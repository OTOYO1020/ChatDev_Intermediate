import random
class Game:
    def __init__(self):
        self.secret_number = self.generate_secret_number()
        self.remaining_lives = 7
    def generate_secret_number(self):
        digits = random.sample(range(1, 10), 3)
        secret_number = ''.join(map(str, digits))
        return secret_number
    def check_guess(self, guess):
        if len(guess) != 3 or not guess.isdigit():
            return False, "Invalid input. Please enter a three-digit number."
        hits = 0
        blows = 0
        for i in range(3):
            if guess[i] == self.secret_number[i]:
                hits += 1
            elif guess[i] in self.secret_number:
                blows += 1
        self.remaining_lives -= 1
        if hits == 3:
            return True, "Congratulations! You guessed the number correctly."
        elif self.remaining_lives == 0:
            return True, f"Game over. The secret number was {self.secret_number}."
        else:
            return False, f"Hits: {hits}, Blows: {blows}. Remaining lives: {self.remaining_lives}"