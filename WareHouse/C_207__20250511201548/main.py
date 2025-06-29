'''
Main entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
from gomoku_gui import GomokuGUI
def main():
    game = GomokuGame()
    mode = input("Choose mode: 1 for Console, 2 for GUI: ")
    if mode == '1':
        game.run()  # Run the game logic without GUI
    elif mode == '2':
        gui = GomokuGUI(game)
        gui.run()  # Run the GUI
    else:
        print("Invalid mode selected. Exiting.")
if __name__ == "__main__":
    main()