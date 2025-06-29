def check_guess(self, guess):
    hits = 0
    blows = 0
    for i in range(3):
        if guess[i] == self.generated_number[i]:
            hits += 1
        elif guess[i] in self.generated_number:
            blows += 1
    self.remaining_lives -= 1
    self.last_guess = guess
    return hits, blows