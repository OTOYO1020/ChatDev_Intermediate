'''
Main application file for the card game using standard input and output.
'''
from typing import List  # Importing List for type hinting
from game_logic import find_eaten_cards
def main():
    try:
        n = int(input("Number of Cards (N): "))
        k = int(input("Threshold for Eating Cards (K): "))
        p = list(map(int, input("List of Cards (P) - comma separated: ").split(',')))
        if len(p) != n:
            raise ValueError("The number of cards does not match N.")
        eaten_moves = find_eaten_cards(n, k, p)
        display_results(eaten_moves)
    except Exception as e:
        print(f"Error: {str(e)}")
def display_results(eaten_moves: List[int]):
    if any(move != -1 for move in eaten_moves):
        print("Eaten Moves: " + ', '.join(map(str, eaten_moves)))
    else:
        print("No cards were eaten.")
if __name__ == "__main__":
    main()