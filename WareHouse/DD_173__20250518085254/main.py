'''
Main entry point for the comfort calculation application.
'''
from comfort_calculator import ComfortCalculator
def main():
    N = int(input("Enter the number of players: "))
    A = list(map(int, input("Enter the friendliness values (comma-separated): ").split(',')))
    calculator = ComfortCalculator()
    result = calculator.max_total_comfort(N, A)
    print(f"Maximum Total Comfort: {result}")
if __name__ == "__main__":
    main()