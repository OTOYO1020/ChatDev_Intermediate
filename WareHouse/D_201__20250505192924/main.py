'''
Main entry point for the game application.
'''
from game import Game  # Import the Game class
def main():
    h = int(input("Enter grid height (H): "))
    w = int(input("Enter grid width (W): "))
    grid = []
    # Collect grid values from user input
    for i in range(h):
        row_values = input(f"Enter row {i + 1} values (+ or -): ").strip().split()
        if len(row_values) != w or any(val not in ['+', '-'] for val in row_values):
            print("Invalid input. Please enter exactly {} values of '+' or '-'.".format(w))
            return  # Exit if the input is invalid
        grid.append(row_values)
    game = Game(h, w, grid)
    game.play_game(0, 0, 0)
    result = game.get_winner()
    print(f"The winner is: {result}")
if __name__ == "__main__":
    main()