'''
Main application file for the Valid Integer Counter.
'''
import sys
from counter import count_valid_integers
def main():
    try:
        N = int(input("Enter an integer N (2 <= N <= 10^6): "))
        if N < 2 or N > 10**6:
            raise ValueError("N must be between 2 and 10^6.")
        result = count_valid_integers(N)
        print(f"Count of valid integers of length {N}: {result}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()