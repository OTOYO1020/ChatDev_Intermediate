'''
Main application file for the string shift application.
'''
from shift_utils import ShiftUtils  # Import ShiftUtils for string shifting utilities
class MainApp:
    def __init__(self):
        self.shift_utils = ShiftUtils()
    def compute_shifts(self):
        s = input("Enter a non-empty string: ").strip()  # Strip whitespace
        if not s:
            print("Input Error: Please enter a non-empty string.")
            return
        smallest = largest = s
        try:
            # Compute left shifts
            for i in range(len(s)):
                left_shifted = self.shift_utils.left_shift(s, i)
                if left_shifted < smallest:  # Update smallest if left_shifted is smaller
                    smallest = left_shifted
                if left_shifted > largest:  # Update largest if left_shifted is larger
                    largest = left_shifted
            # Compute right shifts
            for i in range(len(s)):
                right_shifted = self.shift_utils.right_shift(s, i)
                if right_shifted < smallest:  # Update smallest if right_shifted is smaller
                    smallest = right_shifted
                if right_shifted > largest:  # Update largest if right_shifted is larger
                    largest = right_shifted
            print(f"Smallest: {smallest}, Largest: {largest}")
        except ValueError as e:
            print(f"Error: {e}")
    def run(self):
        self.compute_shifts()
if __name__ == "__main__":
    app = MainApp()
    app.run()