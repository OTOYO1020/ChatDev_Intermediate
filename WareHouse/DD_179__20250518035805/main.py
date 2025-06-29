'''
Main entry point of the application.
'''
import tkinter as tk
from input_frame import InputFrame
from output_frame import OutputFrame
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Count Ways Application")
        self.input_frame = InputFrame(self.root, self.calculate_ways)
        self.input_frame.pack()
        self.output_frame = OutputFrame(self.root)
        self.output_frame.pack()
    def calculate_ways(self, N, K, segments):
        from logic import countWays
        result = countWays(N, K, segments)
        self.output_frame.display_result(result)
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()