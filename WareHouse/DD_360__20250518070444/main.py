'''
Main entry point for the Ant Passing application.
'''
from tkinter import Tk, Label, Entry, Button, Text, END
from ant_passing import count_passing_pairs
class AntPassingApp:
    def __init__(self, master):
        self.master = master
        master.title("Ant Passing Pairs Calculator")
        self.label = Label(master, text="Enter N, T, S, and X (comma-separated):")
        self.label.pack()
        self.entry = Entry(master)
        self.entry.pack()
        self.calculate_button = Button(master, text="Calculate Passing Pairs", command=self.calculate_pairs)
        self.calculate_button.pack()
        self.result_text = Text(master, height=10, width=50)
        self.result_text.pack()
    def calculate_pairs(self):
        input_data = self.entry.get()
        try:
            # Parse input
            parts = input_data.split(',')
            N = int(parts[0].strip())
            T = float(parts[1].strip())
            S = parts[2].strip()
            X = list(map(int, parts[3].strip().split()))
            # Validate input
            if N <= 0:
                raise ValueError("N must be greater than zero.")
            if len(S) != N or len(X) != N:
                raise ValueError("Invalid input lengths.")
            if not all(c in '01' for c in S):
                raise ValueError("S must be a binary string.")
            if len(set(X)) != N:
                raise ValueError("X must contain distinct integers.")
            if any(x < 0 for x in X):  # Ensure all integers in X are non-negative
                raise ValueError("All elements in X must be non-negative integers.")
            # Calculate passing pairs
            result = count_passing_pairs(N, T, S, X)
            self.result_text.delete(1.0, END)
            self.result_text.insert(END, f"Number of passing pairs: {result}")
        except Exception as e:
            self.result_text.delete(1.0, END)
            self.result_text.insert(END, f"Error: {str(e)}")
if __name__ == "__main__":
    root = Tk()
    app = AntPassingApp(root)
    root.mainloop()