'''
Main entry point for the game application.
'''
from game_logic import GameLogic
def main():
    while True:  # Loop until valid input is received
        try:
            A, B, C, D = map(int, input("Enter A, B, C, D separated by spaces: ").split())
            if A > B or C > D:
                raise ValueError("Invalid ranges: A should be <= B and C should be <= D.")
            break  # Exit loop if input is valid
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter four integers separated by spaces.")
    game_logic = GameLogic(A, B, C, D)
    game_logic.calculate_winning_moves()
    winner = game_logic.determine_winner()
    print(f"The winner is: {winner}")
if __name__ == "__main__":
    main()