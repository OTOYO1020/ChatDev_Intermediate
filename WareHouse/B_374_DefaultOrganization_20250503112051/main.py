'''
Main application file for the string comparison application.
'''
import sys
from string_comparator import compare_strings
def main():
    '''
    Main function to read input strings and compare them.
    '''
    while True:
        try:
            # Read two strings from standard input
            S = input("Enter the first string: ")
            T = input("Enter the second string: ")
            if S == "" or T == "":
                print("Both strings must be non-empty. Please try again.")
                continue  # Prompt again if either string is empty
            break  # Exit the loop if inputs are valid
        except Exception as e:
            print(f"An error occurred: {e}")  # Print the error message and prompt again
    # Compare the strings and print the result
    result = compare_strings(S, T)
    if result == 0:
        print("The strings are equal.")
    else:
        print(f"Result: {result}")
if __name__ == "__main__":
    main()