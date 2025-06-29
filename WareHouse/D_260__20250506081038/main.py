'''
Main entry point for the card game application.
'''
import sys
from card_game import CardGame
from output_frame import OutputFrame
from input_frame import InputFrame
import tkinter as tk
def handle_game(N, K, P, output_frame):
    game = CardGame(N, K, P)
    results = game.play_game()
    output_frame.update_output(results)
def main():
    root = tk.Tk()
    output_frame = OutputFrame(root)
    output_frame.pack()
    input_frame = InputFrame(root, lambda N, K, P: handle_game(N, K, P, output_frame))
    input_frame.pack()
    root.mainloop()
if __name__ == "__main__":
    main()