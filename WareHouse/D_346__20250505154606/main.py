'''
Main application file for the Good String Converter.
'''
import sys
from utils import validate_input, calculate_cost
def main():
    '''
    Main function to read input and calculate the minimum cost to convert the string into a good string.
    '''
    # Read inputs from standard input
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    c = list(map(int, sys.stdin.readline().strip().split(',')))
    if validate_input(n, s, c):
        min_cost = calculate_cost(n, s, c)
        if min_cost == -1:
            print("No good string can be formed.")
        else:
            print(f"Minimum Cost: {min_cost}")
    else:
        print("Input Error: Please ensure all inputs are valid.")
if __name__ == "__main__":
    main()