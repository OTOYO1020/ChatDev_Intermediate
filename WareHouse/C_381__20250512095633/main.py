'''
Main application file for the 11/22 string finder.
'''
import sys
from utils import max_11_22_length
def main():
    input_string = input("Enter a string (1 ≤ length ≤ 200,000, must contain at least one '/'): ")
    if len(input_string) < 1 or len(input_string) > 200000:
        print("Input Error: String length must be between 1 and 200,000.", file=sys.stderr)
        return
    try:
        max_length = max_11_22_length(input_string)
        if max_length == 0:
            print("No valid 11/22 substring found.")
        else:
            print(f"Max Length: {max_length}")
    except ValueError as e:
        print(f"Input Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    main()