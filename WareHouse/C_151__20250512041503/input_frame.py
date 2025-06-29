'''
Module for the input frame of the application.
'''
import tkinter as tk
from submission import SubmissionEntry
class InputFrame(tk.Frame):
    def __init__(self, master, calculate_callback):
        super().__init__(master)
        self.calculate_callback = calculate_callback
        self.label = tk.Label(self, text="Enter submissions (format: problem_id verdict):")
        self.label.pack()
        self.text_area = tk.Text(self, height=10, width=50)
        self.text_area.pack()
        self.n_label = tk.Label(self, text="Enter number of problems (N):")
        self.n_label.pack()
        self.n_entry = tk.Entry(self)
        self.n_entry.pack()
        self.m_label = tk.Label(self, text="Enter number of submissions (M):")
        self.m_label.pack()
        self.m_entry = tk.Entry(self)
        self.m_entry.pack()
        self.calculate_button = tk.Button(self, text="Calculate Results", command=self.on_calculate)
        self.calculate_button.pack()
    def get_submissions(self):
        submissions = []
        input_data = self.text_area.get("1.0", tk.END).strip().splitlines()
        for line in input_data:
            if line:
                try:
                    problem_id, verdict = line.split()
                    submissions.append((int(problem_id), verdict))  # Store as tuple
                except ValueError:
                    print(f"Invalid input format: {line}")  # Handle input errors
        return submissions
    def on_calculate(self):
        try:
            N = int(self.n_entry.get())  # Get N from user input
            M = int(self.m_entry.get())  # Get M from user input
            results = self.calculate_callback(N, M)
            self.result_frame.display_results(*results)  # Display results in the result frame
        except ValueError:
            print("Please enter valid integers for N and M.")