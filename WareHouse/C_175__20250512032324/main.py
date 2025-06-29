'''
Main application file for the minimum absolute coordinate calculator.
'''
from calculator import minimum_absolute_coordinate
def main():
    '''
    Main function to handle input and output.
    '''
    try:
        # Read input values from standard input
        x, k, d = map(int, input("Enter X, K, D separated by spaces: ").split())
        result = minimum_absolute_coordinate(x, k, d)
        print(f"Result: {result}")
    except ValueError:
        print("Input Error: Please enter valid integers for X, K, and D.")
if __name__ == "__main__":
    main()