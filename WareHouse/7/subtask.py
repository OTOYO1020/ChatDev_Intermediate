import random
def generate_random_number():
    digits = random.sample(range(1, 10), 3)
    return "".join(map(str, digits))
def check_guess(guess, target):
    hits = 0
    blows = 0
    for i in range(3):
        if guess[i] == target[i]:
            hits += 1
        elif guess[i] in target:
            blows += 1
    return {"hits": hits, "blows": blows}