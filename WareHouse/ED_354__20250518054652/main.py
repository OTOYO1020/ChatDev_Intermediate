'''
Main entry point of the card game application using standard input and output.
'''
from game_logic import GameLogic
def main():
    # Read input values
    N = int(input("Enter the number of cards: "))
    A = list(map(int, input("Enter the front values of the cards (space-separated): ").split()))
    B = list(map(int, input("Enter the back values of the cards (space-separated): ").split()))
    # Create an instance of GameLogic and determine the winner
    game_logic = GameLogic()
    winner = game_logic.determine_winner(N, A, B)
    print(f"The winner is: {winner}")
if __name__ == "__main__":
    main()