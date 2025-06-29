def validate_input(self, guess):
    if len(guess) != 3 or not guess.isdigit():
        return False
    if len(set(guess)) != 3:
        return False
    return True