'''
Main entry point for the command-line application.
'''
from combinatorial_calculator import CombinatorialCalculator
def main():
    k = int(input("Enter K (number of blue balls): "))
    n = int(input("Enter N (total number of balls): "))
    calculator = CombinatorialCalculator()
    ways = calculator.calculate_ways(k, n)
    print("Ways to arrange:")
    for way in ways:
        print(way)
if __name__ == "__main__":
    main()