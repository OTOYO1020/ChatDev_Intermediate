'''
Main application file for the Dango String Analyzer.
'''
import sys
from dango_analyzer import DangoStringAnalyzer
def main():
    '''
    Entry point of the application.
    Reads input from standard input and analyzes the dango string.
    '''
    try:
        n = int(input("Enter an integer N (length of string to analyze): "))
        s = input("Enter a string S (containing '-' and 'o' only): ")[:n]  # Limit to first N characters
        if not s:  # Check if the string is empty
            print("Input Error: The string S cannot be empty.")
            return  # Exit the method if S is empty
        # Inform the user about the length of the string being analyzed
        if n < len(s):
            print(f"Warning: Analyzing the first {n} characters of the string S.")
        # Validate characters in S
        if any(char not in ('-', 'o') for char in s):
            print("Input Error: The string S must contain only '-' and 'o' characters.")
            return  # Exit if invalid characters are found
        analyzer = DangoStringAnalyzer(s)
        result = analyzer.find_greatest_level()
        print(f"Greatest level of dango string: {result}")
    except ValueError:
        print("Input Error: Please enter a valid integer for N.")
if __name__ == "__main__":
    main()