'''
Main entry point for the stone removal game application.
'''
from game import Game
def main():
    while True:
        try:
            n = int(input("Enter the number of stones (N): "))
            if n <= 0:
                raise ValueError("The number of stones must be a positive integer.")
            k = int(input("Enter the number of possible moves (K): "))
            if k <= 0:
                raise ValueError("The number of possible moves must be a positive integer.")
            moves = list(map(int, input("Enter the possible moves separated by space: ").split()))
            if len(moves) != k:
                raise ValueError(f"Expected {k} moves, but got {len(moves)}.")
            break  # Exit the loop if inputs are valid
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    # Create a Game instance and play
    game = Game(n, moves)
    takahashi_stones = game.play_game()
    # Output the result
    print(f"Takahashi removed {takahashi_stones} stones.")
if __name__ == "__main__":
    main()