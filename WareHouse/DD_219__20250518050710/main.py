'''
Main application file for the Lunchbox command-line application.
'''
import sys
from lunchbox import can_buy_lunchboxes
def main():
    try:
        # Parse input from command line arguments
        N = int(sys.argv[1])
        X = int(sys.argv[2])
        Y = int(sys.argv[3])
        A = list(map(int, sys.argv[4].split(',')))
        B = list(map(int, sys.argv[5].split(',')))
        possible, min_lunchboxes = can_buy_lunchboxes(N, X, Y, A, B)
        # Format the output based on the result
        if possible:
            print(f"Possible to buy lunchboxes. Minimum needed: {min_lunchboxes}")
        else:
            print("Not possible to buy the required lunchboxes.")
    except ValueError as e:
        print(f"Input Error: {e}. Please provide valid inputs in the format: N X Y A B")
    except IndexError:
        print("Input Error: Please provide all required inputs.")
if __name__ == "__main__":
    main()