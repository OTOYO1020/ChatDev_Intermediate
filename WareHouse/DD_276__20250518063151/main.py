'''
Main application file to run the Equalizer application.
'''
from equalizer import min_operations_to_equalize
import sys
from typing import List
def main():
    input_text = sys.stdin.read()
    try:
        A = list(map(int, input_text.split()))
        result = min_operations_to_equalize(A)
        print(result)
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()