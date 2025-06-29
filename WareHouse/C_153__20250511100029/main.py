'''
This is the main entry point for the Gomoku game application.
'''
from gomoku import GomokuGame
import tkinter as tk
def main():
    choice = input("Choose mode: (1) Console (2) GUI: ")
    if choice == '1':
        game = GomokuGame()
        while True:
            game.print_board()
            try:
                row = int(input(f"Player {game.current_player}, enter your move row (0-14): "))
                col = int(input(f"Player {game.current_player}, enter your move column (0-14): "))
                result = game.make_move(row, col)
                if result:
                    print(result)
                    if "wins" in result:
                        game.print_board()
                        break
            except ValueError:
                print("Invalid input! Please enter numbers between 0 and 14.")
    elif choice == '2':
        from gomoku_gui import GomokuGUI
        root = tk.Tk()
        gui = GomokuGUI(root)
        root.mainloop()
    else:
        print("Invalid choice! Please select 1 or 2.")
if __name__ == "__main__":
    main()