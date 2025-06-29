'''
Main entry point for the application.
'''
import tkinter as tk  # Import tkinter
from typing import List, Tuple
from input_frame import InputFrame  # Import InputFrame
from output_frame import OutputFrame  # Import OutputFrame
from graph import Graph
class MainApp:
    def __init__(self):
        self.root = tk.Tk()  # Initialize the root window
        self.input_frame = InputFrame(self.run_max_operations)
        self.output_frame = OutputFrame()
        # Pack the frames into the root window
        self.input_frame.pack()
        self.output_frame.pack()
    def run_max_operations(self):
        N, M, edges, weights, pieces = self.input_frame.get_input()
        graph = Graph(N, M, edges, weights, pieces)
        result = graph.max_operations()
        self.output_frame.display_result(result)
    def run(self):
        self.root.mainloop()  # Start the Tkinter main loop
if __name__ == "__main__":
    app = MainApp()
    app.run()