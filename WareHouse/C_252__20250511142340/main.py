'''
This is the main entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
from gomoku_gui import GomokuGUI
import tkinter as tk
def run_console():
    game = GomokuGame()
    while True:
        game.print_board()
        if game.winner:
            print(f"Player {game.winner} wins!")
            break
        if game.is_full():
            print("The game is a draw!")
            break
        try:
            row = int(input(f"Player {game.current_player}, enter your move row (0-14): "))
            col = int(input(f"Player {game.current_player}, enter your move column (0-14): "))
            game.make_move(row, col)
        except ValueError as e:
            print(e)  # Display the error message for out of bounds
        except IndexError:
            print("Invalid input! Please enter numbers between 0 and 14.")
def run_gui():
    root = tk.Tk()
    gui = GomokuGUI(root)
    root.mainloop()
if __name__ == "__main__":
    choice = input("Enter '1' for Console Mode or '2' for GUI Mode: ")
    if choice == '1':
        run_console()
    elif choice == '2':
        run_gui()
    else:
        print("Invalid choice! Exiting.")