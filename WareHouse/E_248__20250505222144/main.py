'''
Main application file that handles user interactions via standard input and output.
'''
from input_handler import InputHandler
from line_calculator import LineCalculator
from output_display import OutputDisplay
def main():
    input_handler = InputHandler()
    line_calculator = LineCalculator()
    output_display = OutputDisplay()  # Instantiate OutputDisplay
    try:
        N = int(input("Enter number of points (N): "))
        K = int(input("Enter minimum number of points on a line (K): "))  # Read K
        points = input_handler.get_points(N)
        valid_lines = line_calculator.calculate_lines(points, K)  # Pass K to the method
        output_display.show_result(valid_lines)  # Use OutputDisplay to show results
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()