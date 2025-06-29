'''
Main entry point of the application.
'''
from tkinter import Tk
from input_frame import InputFrame
from output_frame import OutputFrame
class MainApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Cost Calculation Dashboard")
        self.input_frame = InputFrame(self.root, self.run_algorithm)
        self.input_frame.pack()
        self.output_frame = OutputFrame(self.root)
        self.output_frame.pack()
    def run_algorithm(self):
        n, m, constraints = self.input_frame.get_input()
        if constraints is None or n is None or m is None:  # Check if inputs are valid
            return  # Exit the method if inputs are invalid
        from algorithm import Algorithm
        algorithm = Algorithm(n, m, constraints)
        min_cost = algorithm.calculate_min_cost()
        self.output_frame.display_result(min_cost)
        self.input_frame.reset_constraints()  # Clear constraints after running the algorithm
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = MainApp()
    app.run()