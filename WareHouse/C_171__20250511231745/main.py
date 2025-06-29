'''
This is the main entry point of the Gomoku game application.
'''
from gomoku import GomokuGame
import tkinter as tk
def main():
    while True:  # Loop until a valid choice is made
        choice = input("Enter '1' for Console version or '2' for GUI version: ")
        if choice == '1':
            game = GomokuGame()
            while True:
                game.print_board()
                try:
                    row = int(input(f"Player {game.current_player}, enter your move row (0-14): "))
                    col = int(input(f"Player {game.current_player}, enter your move column (0-14): "))
                    result = game.make_move(row, col)
                    if result:
                        game.print_board()
                        print(result)
                        break
                except (ValueError, IndexError):
                    print("Invalid move. Please try again.")
            break  # Exit the loop after the console game ends
        elif choice == '2':
            root = tk.Tk()
            gui = GomokuGUI(root)
            root.mainloop()
            break  # Exit the loop after the GUI game ends
        else:
            print("Invalid choice. Please try again.")  # Prompt again for a valid choice
if __name__ == "__main__":
    main()