'''
Main application file for calculating Manhattan distances.
'''
from distance_calculator import DistanceCalculator
def main():
    # Receive integers N, M, and K from standard input
    n = int(input("Please enter the number of rows (N): "))
    m = int(input("Please enter the number of columns (M): "))
    k = int(input("Please enter the number of pieces (K): "))
    # Create an instance of DistanceCalculator
    calculator = DistanceCalculator(n, m, k)
    # Calculate the total Manhattan distance
    result = calculator.calculate_distance()
    # Output the result
    print(f"Total Manhattan Distance: {result}")
if __name__ == "__main__":
    main()