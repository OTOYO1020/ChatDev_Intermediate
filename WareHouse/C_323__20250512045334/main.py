'''
Main application file for the Score Calculator.
'''
from tkinter import Tk, Label, Entry, Button, Text, END
from score_calculator import calculate_min_problems_to_solve
class ScoreCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Score Calculator")
        self.label_n = Label(master, text="Number of Players (N):")
        self.label_n.pack()
        self.entry_n = Entry(master)
        self.entry_n.pack()
        self.label_m = Label(master, text="Number of Problems (M):")
        self.label_m.pack()
        self.entry_m = Entry(master)
        self.entry_m.pack()
        self.label_scores = Label(master, text="Scores (comma-separated):")
        self.label_scores.pack()
        self.entry_scores = Entry(master)
        self.entry_scores.pack()
        self.label_solved = Label(master, text="Solved Problems (comma-separated):")
        self.label_solved.pack()
        self.entry_solved = Entry(master)
        self.entry_solved.pack()
        self.calculate_button = Button(master, text="Calculate", command=self.calculate_scores)
        self.calculate_button.pack()
        self.result_text = Text(master, height=10, width=50)
        self.result_text.pack()
    def calculate_scores(self):
        try:
            N = int(self.entry_n.get())
            M = int(self.entry_m.get())
            scores = list(map(int, self.entry_scores.get().split(',')))
            solved = self.entry_solved.get().split(',')
            results = calculate_min_problems_to_solve(N, M, scores, solved)
            self.result_text.delete(1.0, END)
            self.result_text.insert(END, f"Minimum Problems to Solve: {results}")
        except Exception as e:
            self.result_text.delete(1.0, END)
            self.result_text.insert(END, f"Error: {str(e)}")
if __name__ == "__main__":
    root = Tk()
    app = ScoreCalculatorApp(root)
    root.mainloop()