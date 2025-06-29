'''
This module contains the main function to run the Gomoku game in the console or GUI.
'''
from gomoku_game import GomokuGame
import tkinter as tk
def main():
    choice = input("Do you want to play in console (C) or GUI (G)? ").strip().lower()
    if choice == 'g':
        from gomoku_gui import GomokuGUI
        root = tk.Tk()
        root.title("Gomoku Game")
        gui = GomokuGUI(root)
        root.mainloop()
    else:
        game = GomokuGame()
        while True:
            game.display_board()
            try:
                x, y = map(int, input(f"Player {game.current_player}, enter your move (row and column): ").split())
                result = game.make_move(x, y)
                if result:
                    print(result)
                    game.display_board()
                    reset = input("Do you want to play again? (yes/no): ").strip().lower()
                    if reset == 'yes':
                        game.reset_game()
                    else:
                        break
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column numbers between 0 and 14.")
if __name__ == "__main__":
    main()