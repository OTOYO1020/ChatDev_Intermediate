'''
Main application file for the Distance Calculator.
'''
import sys  # Import sys for graceful termination
from distance_calculator import DistanceCalculator
def main():
    # Create an instance of DistanceCalculator
    calculator = DistanceCalculator()
    # Read points p and q from standard input
    p = ''
    q = ''
    # Loop until valid input for p
    while True:
        p = input("Enter point p (A-G): ").strip().upper()
        if len(p) == 1 and p in calculator.point_index:
            break
        print("Invalid input for point p. Please enter a single uppercase letter (A-G).")
    # Loop until valid input for q
    while True:
        q = input("Enter point q (A-G): ").strip().upper()
        if len(q) == 1 and q in calculator.point_index:
            break
        print("Invalid input for point q. Please enter a single uppercase letter (A-G).")
    # Calculate distance
    try:
        distance = calculator.calculate(p, q)
        print(f"Distance between {p} and {q}: {distance}")
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()