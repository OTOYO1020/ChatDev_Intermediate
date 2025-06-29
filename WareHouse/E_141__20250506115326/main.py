'''
Main application file for the substring finder application.
'''
import sys
from substring_finder import SubstringFinder
def main():
    try:
        n = int(input("Enter an integer N (length of the string): "))
        s = input("Enter a string S: ")
        if len(s) < n:
            raise ValueError("String length must be at least N.")
        finder = SubstringFinder(s)
        max_length = finder.max_non_overlapping_length()
        print(f"Max Length of non-overlapping substring: {max_length}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()