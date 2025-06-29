'''
Main entry point of the application that initializes the console and manages user interactions.
'''
import sys
from input_handler import InputHandler
from cost_calculator import CostCalculator
def main():
    try:
        N = int(input("Enter the number of boxes and items: "))
        box_numbers = input("Enter box numbers (space-separated): ")
        item_weights = input("Enter item weights (space-separated): ")
        input_handler = InputHandler()
        boxes, weights = input_handler.get_input(N, box_numbers, item_weights)
        cost_calculator = CostCalculator()
        total_cost = cost_calculator.calculate(boxes, weights)
        print(f"The total minimum cost is: {total_cost}")
    except ValueError as ve:
        print(f"Input Error: {str(ve)}. Please ensure the number of boxes and weights match N.")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()