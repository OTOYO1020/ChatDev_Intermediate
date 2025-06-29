'''
Main application file for the Bounce Calculator.
'''
from bounce_calculator import BounceCalculator
def read_input():
    """
    Read integers N and X from standard input, followed by a list of integers L of length N.
    Returns N, X, and L.
    """
    n = int(input("Enter N (number of bounces): "))
    x = int(input("Enter X (max coordinate): "))
    l = list(map(int, input("Enter L (bounce distances, comma-separated): ").split(',')))
    if len(l) != n:
        raise ValueError("Length of L must be equal to N.")
    return n, x, l
def main():
    """
    Main function to execute the bounce calculation.
    """
    try:
        n, x, l = read_input()
        calculator = BounceCalculator()
        bounce_count = calculator.calculate_bounces(n, x, l)
        print(f"Number of bounces: {bounce_count}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()