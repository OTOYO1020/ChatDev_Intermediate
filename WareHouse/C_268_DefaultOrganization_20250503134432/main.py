'''
Main application file for the Happy People Calculator.
'''
import sys
from input_validation import InputValidation
from output_display import OutputDisplay
class MainApp:
    def calculate_happy_people(self, n, p, m):
        '''
        Calculate the number of happy people based on dish positions.
        '''
        happy_count = 0
        for i in range(n):
            # Check if the dish in front of person i is also in front of themselves or their neighbors
            if p[i] in (p[(i - 1) % n], p[i], p[(i + 1) % n]):
                happy_count += 1
        result = happy_count % m
        return result
if __name__ == "__main__":
    try:
        n = int(input("Enter number of people (N): "))
        # Improved prompt for dish positions
        p_input = input("Enter dish positions (comma-separated integers): ")
        try:
            p = list(map(int, p_input.split(',')))
        except ValueError:
            raise ValueError("Dish positions must be a list of integers separated by commas.")
        m = int(input("Enter value of m: "))
        # Validate inputs
        validator = InputValidation()
        validator.validate_input(n, p, m)
        app = MainApp()
        result = app.calculate_happy_people(n, p, m)
        # Display result
        output_display = OutputDisplay()
        output_display.show_result(result)
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")