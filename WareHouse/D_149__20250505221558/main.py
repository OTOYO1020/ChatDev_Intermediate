'''
Main entry point for the Rock-Paper-Scissors game application.
'''
from game_logic import GameLogic
def main():
    # Read integers N, K, R, S, P from standard input
    N, K, R, S, P = map(int, input("Enter N, K, R, S, P: ").split())
    # Read the string T of length N
    T = input("Enter the machine's moves (string of length N): ").strip()
    # Create an instance of GameLogic
    game_logic = GameLogic(R, S, P)
    # Calculate the maximum score
    max_score = game_logic.calculate_max_score(N, K, T)
    # Print the max_score as the output
    print(f"Max Score: {max_score}")
if __name__ == "__main__":
    main()