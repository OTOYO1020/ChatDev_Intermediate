'''
Main application file for the tastiness checker.
'''
import sys
from data_processor import DataProcessor  # Importing the DataProcessor class
class MainApplication:
    def __init__(self):
        self.n = 0
        self.k = 0
        self.tastiness_values = []
        self.disliked_indices = []
    def read_input(self):
        try:
            self.n, self.k = map(int, input().split())
            if self.n < 0 or self.k < 0:
                print("Error: N and K must be non-negative integers.", file=sys.stderr)
                return
            if self.n == 0:
                print("No tastiness values provided.")
                return  # Exit early if there are no tastiness values
            # Read tastiness values
            tastiness_input = input().strip()
            if not tastiness_input:
                print("Error: Tastiness values must be provided.", file=sys.stderr)
                return
            self.tastiness_values = list(map(int, tastiness_input.split()))
            if len(self.tastiness_values) != self.n:
                print(f"Error: Expected {self.n} tastiness values, but got {len(self.tastiness_values)}.", file=sys.stderr)
                return
            if any(value < 0 for value in self.tastiness_values):
                print("Error: Tastiness values must be non-negative.", file=sys.stderr)
                return
            # Read disliked indices
            disliked_input = input().strip()
            if not disliked_input:
                print("Error: Disliked food indices must be provided.", file=sys.stderr)
                return
            self.disliked_indices = list(map(int, disliked_input.split()))
            if len(self.disliked_indices) != self.k:
                print(f"Error: Expected {self.k} disliked food indices, but got {len(self.disliked_indices)}.", file=sys.stderr)
                return
            # Validate indices in B
            if any(index < 0 or index >= self.n for index in self.disliked_indices):
                print("Error: Disliked food indices must be in the range of 0 to N-1.", file=sys.stderr)
                return
        except ValueError:
            print("Error: Invalid input format. Please enter integers for N, K, tastiness values, and disliked indices.", file=sys.stderr)
    def check_disliked_food(self):
        processor = DataProcessor(self.tastiness_values, self.disliked_indices)  # Use DataProcessor
        has_disliked_food = processor.check_disliked_food()
        return has_disliked_food
    def run(self):
        try:
            self.read_input()
            if self.n == 0:  # Check if N is 0 to avoid further processing
                return
            has_disliked_food = self.check_disliked_food()
            print("Yes" if has_disliked_food else "No")
        except Exception as e:
            print(f"Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    app = MainApplication()
    app.run()