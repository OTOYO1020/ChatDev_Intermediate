'''
Main entry point for the application.
'''
import sys
from input_handler import InputHandler
from cost_calculator import CostCalculator
def main():
    input_handler = InputHandler()
    bags, target_string = input_handler.get_input()
    cost_calculator = CostCalculator()
    min_cost = cost_calculator.min_cost_to_form_string(len(bags), bags, target_string)
    print(min_cost)
if __name__ == "__main__":
    main()