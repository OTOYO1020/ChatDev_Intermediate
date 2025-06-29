'''
Main application file for the Box Counter.
'''
from data_processor import DataProcessor  # Import the DataProcessor class
class MainApp:
    def __init__(self):
        self.data = []
        self.load_data()
    def load_data(self):
        # Read H and W from standard input
        while True:
            try:
                H, W = map(int, input("Enter number of rows (H) and columns (W): ").split())
                if H <= 0 or W <= 0:
                    raise ValueError("H and W must be positive integers.")
                break
            except ValueError as e:
                print(f"Error: {e}. Please enter valid integers for H and W.")
        self.data = []
        # Read the grid data
        print("Enter the grid row by row (use '#' for boxes and '.' for empty spaces):")
        for i in range(H):
            while True:  # Loop until a valid row is entered
                row = input(f"Enter row {i + 1} (exactly {W} characters, only '#' and '.'): ").strip()
                if len(row) != W or any(c not in ['#', '.'] for c in row):
                    print(f"Error: Row must have exactly {W} characters and contain only '#' or '.'. Please re-enter.")
                else:
                    self.data.append(list(row))
                    break  # Exit the loop if the row is valid
        processor = DataProcessor(self.data)
        try:
            results = processor.count_boxes()
            self.display_results(results)
        except ValueError as e:
            print(f"Error: {e}")
    def display_results(self, results):
        print("Box counts: " + " ".join(map(str, results)))
if __name__ == "__main__":
    app = MainApp()