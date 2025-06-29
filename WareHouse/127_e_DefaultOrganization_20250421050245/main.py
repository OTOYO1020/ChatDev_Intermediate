'''
Main application file for calculating Manhattan distances in a grid.
'''
import sys
from distance_calculator import DistanceCalculator
def main():
    try:
        N = int(input("Enter N (rows): "))
        M = int(input("Enter M (columns): "))
        K = int(input("Enter K (pieces): "))
        if N <= 0 or M <= 0 or K <= 0 or K > N * M:
            raise ValueError("N, M, and K must be positive integers, and K must not exceed N * M.")
        calculator = DistanceCalculator(N, M, K)
        result = calculator.calculate_distance_cost()
        print(f"Total Manhattan Distance: {result % (10**9 + 7)}")  # Output formatted for clarity
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()