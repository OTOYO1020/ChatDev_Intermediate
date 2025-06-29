import random
class Game:
    def __init__(self):
        self.target_number = self.generate_number()
        self.remaining_lives = 7
        self.game_over = False
    def generate_number(self):
        """
        Generate a random three-digit number with different digits.
        """
        digits = random.sample(range(1, 10), 3)
        return int("".join(map(str, digits)))
    def check_guess(self, guess):
        """
        Compare the user's guess with the target number and return the number of hits and blows.
        """
        target_digits = list(str(self.target_number))
        guess_digits = list(str(guess))
        hits = sum(1 for i in range(3) if target_digits[i] == guess_digits[i])
        common_digits = set(target_digits) & set(guess_digits)
        blows = len(common_digits) - hits
        return hits, blows
    def end_game(self, hits):
        """
        End the game and display a message indicating whether the user has won or lost.
        """
        if hits == 3:
            print("Congratulations! You have won the game.")
        elif self.remaining_lives == 0:
            print("Game Over. You have run out of lives.")
        self.game_over = True
game = Game()