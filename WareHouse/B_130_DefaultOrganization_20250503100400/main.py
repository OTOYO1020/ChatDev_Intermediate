'''
Main application file for the Bounce Counting application.
'''
from bounce_calculator import BounceCalculator
def main():
    '''
    Entry point of the application.
    '''
    try:
        n = int(input("Enter number of bounces (N): "))
        if n < 0:
            raise ValueError("N must be a non-negative integer.")
        lengths = []
        if n > 0:
            lengths = list(map(int, input("Enter lengths of bounces (space-separated): ").split()))
            if len(lengths) != n:
                raise ValueError("Number of lengths must match N.")
        x = int(input("Enter coordinate X: "))
        calculator = BounceCalculator()
        bounce_count = calculator.calculate_bounces(lengths, x)
        print(f"Number of bounces <= {x}: {bounce_count}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()