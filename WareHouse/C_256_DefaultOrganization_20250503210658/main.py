'''
Main application file for the Grid Filler application.
'''
import sys
from grid_logic import count_ways
def main():
    '''
    Main function to read input and compute the number of valid configurations.
    '''
    try:
        # Read six integers from standard input
        h1, h2, h3, w1, w2, w3 = map(int, input("Enter six integers (h1, h2, h3, w1, w2, w3): ").split())
        # Ensure that all input values are positive integers
        if any(x <= 0 for x in [h1, h2, h3, w1, w2, w3]):
            raise ValueError("All input values must be positive integers.")
        h = (h1, h2, h3)
        w = (w1, w2, w3)
        # Call the count_ways function and print the result
        total_ways = count_ways(h, w)
        print(total_ways)  # Print only the total number of valid configurations
    except Exception as e:
        print(f"Input Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    main()