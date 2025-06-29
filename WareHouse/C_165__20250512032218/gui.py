'''
Contains the GUI implementation for the application.
'''
import tkinter as tk
from tkinter import messagebox
from score_calculator import ScoreCalculator
class MainApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Max Score Calculator")
        self.calculator = ScoreCalculator()
        # Input fields
        self.label_n = tk.Label(self.window, text="N:")
        self.label_n.pack()
        self.entry_n = tk.Entry(self.window)
        self.entry_n.pack()
        self.label_m = tk.Label(self.window, text="M:")
        self.label_m.pack()
        self.entry_m = tk.Entry(self.window)
        self.entry_m.pack()
        self.label_q = tk.Label(self.window, text="Q:")
        self.label_q.pack()
        self.entry_q = tk.Entry(self.window)
        self.entry_q.pack()
        self.label_queries = tk.Label(self.window, text="Queries (format: a,b,c,d;...):")
        self.label_queries.pack()
        self.entry_queries = tk.Entry(self.window)
        self.entry_queries.pack()
        self.button_calculate = tk.Button(self.window, text="Calculate Max Score", command=self.calculate_max_score)
        self.button_calculate.pack()
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()
    def calculate_max_score(self):
        try:
            N = int(self.entry_n.get())
            M = int(self.entry_m.get())
            Q = int(self.entry_q.get())
            # Validate input bounds
            if N <= 0 or M <= 0 or Q <= 0:
                messagebox.showerror("Input Error", "N, M, and Q must be positive integers.")
                return
            queries_input = self.entry_queries.get()
            # Validate query input format
            queries = []
            for query in queries_input.split(';'):
                if query.strip():  # Avoid empty queries
                    try:
                        queries.append(tuple(map(int, query.split(','))))
                    except ValueError:
                        messagebox.showerror("Input Error", "Invalid query format. Please use a,b,c,d format.")
                        return
            max_score = self.calculator.max_score(N, M, Q, queries)
            self.result_label.config(text=f"Max Score: {max_score}")
        except ValueError as e:
            messagebox.showerror("Input Error", "Please enter valid integers for N, M, Q and queries.")
        except Exception as e:
            messagebox.showerror("Input Error", str(e))
    def run(self):
        self.window.mainloop()