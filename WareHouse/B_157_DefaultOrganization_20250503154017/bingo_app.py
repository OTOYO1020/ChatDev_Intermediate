'''
This module contains the BingoApp class which handles the input and output for the bingo game without a GUI.
'''
from bingo_game import BingoGame
def main():
    # Read the bingo card values
    card = []
    print("Enter the 3x3 bingo card values (3 rows of 3 unique numbers each, space-separated):")
    for _ in range(3):
        while True:
            try:
                row_values = list(map(int, input().split()))
                if len(row_values) == 3 and len(set(row_values)) == 3:
                    card.append(row_values)
                    break
                else:
                    print("Invalid input. Please enter exactly 3 unique numbers for this row.")
            except ValueError:
                print("Invalid input. Please enter only integers.")
    # Check for overall uniqueness in the card
    all_numbers = {num for row in card for num in row}
    if len(all_numbers) != 9:
        print("Invalid input. The bingo card must contain 9 unique numbers.")
        return  # Exit the function if the card is invalid
    # Read the chosen numbers
    print("Enter chosen numbers (space-separated):")
    while True:
        try:
            chosen_numbers = list(map(int, input().split()))
            if len(chosen_numbers) > 0 and len(set(chosen_numbers)) == len(chosen_numbers):  # Ensure at least one number is chosen and unique
                break
            else:
                print("Invalid input. Please enter at least one unique chosen number.")
        except ValueError:
            print("Invalid input. Please enter only integers.")
    # Instantiate BingoGame with the current card and chosen numbers
    bingo_game = BingoGame(card, chosen_numbers)
    bingo_game.mark_numbers()
    # Check for bingo and print the result
    if bingo_game.check_bingo():
        print("BINGO")
    else:
        print("NO BINGO")