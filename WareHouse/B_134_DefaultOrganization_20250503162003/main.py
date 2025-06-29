'''
Main entry point for the Inspector application.
'''
from inspector import calculate_inspectors
def run():
    while True:
        try:
            n = int(input("Enter the number of apple trees (N): "))
            d = int(input("Enter the inspection range (D): "))
            if n <= 0 or d < 0:
                raise ValueError("N must be positive and D must be non-negative.")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    inspectors = calculate_inspectors(n, d)
    print(f"Minimum Inspectors Needed: {inspectors}")
if __name__ == "__main__":
    run()