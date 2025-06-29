'''
Main application file for the expected value calculator.
'''
from input_handler import InputHandler
from calculator import Calculator
class MainApp:
    def __init__(self):
        self.input_handler = InputHandler()
        self.calculator = Calculator()
    def create_widgets(self):
        print("Enter N:")
        n_str = input()
        print("Enter K:")
        k_str = input()
        print("Enter sequence A (space-separated):")
        a_str = input()
        self.calculate(n_str, k_str, a_str)
    def calculate(self, n_str, k_str, a_str):
        N, K, A = self.input_handler.get_input(n_str, k_str, a_str)
        if N is not None and K is not None and A is not None:
            if K > N or K < 1:
                print("Error: K must be between 1 and N.")
                return
            result = self.calculator.compute_expected_value(N, K, A)
            print(f"Result: {result}")
    def run(self):
        self.create_widgets()
if __name__ == "__main__":
    app = MainApp()
    app.run()