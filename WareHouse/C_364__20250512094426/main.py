'''
Main application file for the Dish Selector.
'''
import sys
from dishes import min_dishes
def main():
    try:
        # Read input from standard input
        input_data = sys.stdin.read().strip().splitlines()
        N = int(input_data[0])
        X = int(input_data[1])
        Y = int(input_data[2])
        A = list(map(int, input_data[3].split(',')))
        B = list(map(int, input_data[4].split(',')))
        if len(A) != N or len(B) != N:
            raise ValueError("The length of A and B must match N.")
        result = min_dishes(N, X, Y, A, B)
        print(f"Minimum Dishes Eaten: {result}")
    except Exception as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()