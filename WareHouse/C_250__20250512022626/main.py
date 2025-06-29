'''
Main entry point for the Ball Swapper application.
'''
from ball_swapper import perform_swaps
from input_handler import InputHandler
from output_display import OutputDisplay
if __name__ == "__main__":
    input_handler = InputHandler()
    N, Q, operations = input_handler.get_input()
    final_state = perform_swaps(N, Q, operations)
    output_display = OutputDisplay()
    output_display.display_output(final_state)