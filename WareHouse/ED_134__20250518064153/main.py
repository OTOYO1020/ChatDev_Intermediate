'''
Main application file for the Color Application.
'''
import sys
from color_logic import min_colors_required
def main():
    # Read input from standard input
    input_data = sys.stdin.read().strip()
    # Split the input data by spaces
    input_list = list(map(int, input_data.split()))
    # The first element is N, the rest are the elements of A
    N = input_list[0]
    A = input_list[1:]
    color_count = min_colors_required(N, A)
    print(f"Minimum colors required: {color_count}")
if __name__ == "__main__":
    main()