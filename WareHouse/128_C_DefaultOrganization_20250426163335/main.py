'''
Main entry point of the application that handles user interactions and integrates input handling and switch management.
'''
from bulb import Bulb  # Import the Bulb class
from switch_manager import SwitchManager  # Import the SwitchManager class
from input_handler import InputHandler  # Import the InputHandler class
from output_handler import OutputHandler  # Import the OutputHandler class
class MainApp:
    def __init__(self):
        self.switch_count = 0
        self.bulbs = []
        self.input_handler = InputHandler(self)
        self.switch_manager = SwitchManager()
    def run(self):
        self.input_handler.get_input()  # Gather input
        self.switch_manager.initialize(self.switch_count, self.bulbs)  # Initialize switch manager
        valid_combinations = self.switch_manager.calculate_valid_combinations()  # Calculate valid combinations
        OutputHandler(self).display_result(valid_combinations)  # Display results
if __name__ == "__main__":
    app = MainApp()
    app.run()  # Start the application