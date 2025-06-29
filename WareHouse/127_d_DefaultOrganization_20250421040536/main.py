'''
Main entry point for the card management application.
'''
import sys
import heapq
from card_manager import CardManager
from input_frame import InputFrame  # Import the InputFrame class
from output_frame import OutputFrame  # Import the OutputFrame class
def main():
    # Receiving input and initializing using InputFrame
    input_frame = InputFrame()  # Create an instance of InputFrame
    n, m, a, operations = input_frame.get_input()  # Get input values
    # Managing the current card values
    card_manager = CardManager(n, a)
    max_sum = card_manager.apply_operations(operations)
    # Outputting the final sum using OutputFrame
    output_frame = OutputFrame()
    output_frame.display_result(max_sum)
if __name__ == "__main__":
    main()