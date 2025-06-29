'''
Main application file to run the program for performing operations on a list of integers.
'''
import tkinter as tk
from input_frame import InputFrame
from output_frame import OutputFrame
from operations import perform_operations
class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Integer Operations Dashboard")
        self.input_frame = InputFrame(self.root)
        self.input_frame.pack(pady=10)
        self.output_frame = OutputFrame(self.root)
        self.output_frame.pack(pady=10)
        self.run_button = tk.Button(self.root, text="Run Operations", command=self.perform_operations)
        self.run_button.pack(pady=10)
    def perform_operations(self):
        N, Q, A, operations = self.input_frame.get_input()
        results = perform_operations(N, Q, A, operations)
        self.output_frame.display_results(results)
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = MainApp()
    app.run()