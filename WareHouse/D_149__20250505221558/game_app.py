'''
Contains the GUI for the Rock-Paper-Scissors game application.
'''
from tkinter import Frame, Label, Button, Entry, StringVar
from game_logic import GameLogic
class GameApp:
    def __init__(self, master):
        self.master = master
        master.title("Rock-Paper-Scissors Game")
        self.label = Label(master, text="Enter N, K, R, S, P and T (space-separated):")
        self.label.pack()
        self.input_var = StringVar()
        self.entry = Entry(master, textvariable=self.input_var)
        self.entry.pack()
        self.start_button = Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack()
        self.result_label = Label(master, text="")
        self.result_label.pack()
    def start_game(self):
        inputs = self.input_var.get().split()
        if len(inputs) < 6:
            self.display_result("Invalid input. Please provide N, K, R, S, P and T.")
            return
        try:
            N, K, R, S, P = map(int, inputs[:5])
            T = inputs[5].strip()
            if len(T) != N or any(move not in 'RPS' for move in T):
                self.display_result("Invalid input. Length of T must be equal to N and contain only 'R', 'P', 'S'.")
                return
            game_logic = GameLogic(R, S, P)
            score = game_logic.calculate_max_score(N, K, T)
            self.display_result(score)
        except ValueError:
            self.display_result("Invalid input. Please enter integers for N, K, R, S, P.")
    def display_result(self, score):
        self.result_label.config(text=f"Max Score: {score}")