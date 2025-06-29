'''
Contains the game logic for determining the winner between Takahashi and Aoki.
'''
def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
def determine_winner(A: int, B: int, C: int, D: int) -> str:
    """Determine the winner based on the game logic."""
    takahashi_wins = 0
    aoki_wins = 0
    for takahashi_choice in range(A, B + 1):
        for aoki_choice in range(C, D + 1):
            total = takahashi_choice + aoki_choice
            if is_prime(total):
                aoki_wins += 1
            else:
                takahashi_wins += 1
    if aoki_wins > takahashi_wins:
        return "Aoki"
    else:  # This will handle both the case where Takahashi wins and the tie case
        return "Takahashi"