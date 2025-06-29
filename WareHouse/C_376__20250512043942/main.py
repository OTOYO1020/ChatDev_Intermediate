'''
Main application file for the Toy Box application.
'''
import sys
from toy_box import min_box_size
def main():
    # Read input values from standard input
    input_data = sys.stdin.read().strip().splitlines()
    N = int(input_data[0])
    A = list(map(int, input_data[1].split(',')))
    B = list(map(int, input_data[2].split(',')))
    # Calculate the minimum box size needed
    result = min_box_size(N, A, B)
    # Output the result
    print(result)
if __name__ == "__main__":
    main()