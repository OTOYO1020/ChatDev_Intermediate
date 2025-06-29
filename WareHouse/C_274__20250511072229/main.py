'''
This is the main entry point for the Gomoku game application.
'''
from gomoku_gui import GomokuGUI
def main():
    '''
    Starts the Gomoku game by creating an instance of GomokuGUI and invoking the play_game method.
    '''
    gui = GomokuGUI()
    gui.play_game()
if __name__ == "__main__":
    main()