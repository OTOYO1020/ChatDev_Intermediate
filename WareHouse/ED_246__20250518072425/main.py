'''
Main entry point for the Bishop movement application.
'''
from bishop_game import BishopGame
def main():
    # Example input for testing
    N = 8
    A_x, A_y = 0, 0  # Starting position
    B_x, B_y = 7, 7  # Target position
    S = [
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........"
    ]  # Board configuration
    game = BishopGame(N, A_x, A_y, B_x, B_y, S)
    moves = game.min_moves_bishop()
    print(f"Minimum moves: {moves}")
if __name__ == "__main__":
    main()