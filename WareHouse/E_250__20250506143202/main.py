'''
Main entry point of the application.
'''
import sys
from input_handler import InputHandler
from set_comparison import SetComparison
from output_handler import OutputHandler
class MainApp:
    def __init__(self):
        self.set_comparison = SetComparison()
        self.output_handler = OutputHandler()
    def run(self):
        self.input_handler = InputHandler(self)
        self.input_handler.process_input()
if __name__ == "__main__":
    app = MainApp()
    app.run()