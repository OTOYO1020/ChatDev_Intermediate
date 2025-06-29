'''
Main application file for the LCP Calculator.
'''
from lcp_calculator import lcp, find_max_lcp  # Importing lcp and find_max_lcp
if __name__ == "__main__":
    while True:
        try:
            N = int(input("Enter the number of strings (positive integer): "))
            if N <= 0:
                raise ValueError("The number of strings must be a positive integer.")
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
            continue
    strings = []
    for i in range(N):
        while True:  # Loop until a valid string is entered
            string = input(f"Enter string {i + 1}: ")
            stripped_string = string.strip()  # Strip leading and trailing spaces
            if not stripped_string:  # Check for empty strings after stripping
                print("String cannot be empty. Please enter a valid string.")
                continue  # Prompt for input again
            strings.append(stripped_string)  # Append the valid string
            break  # Exit the loop if a valid string is entered
    max_lcp = find_max_lcp(strings)
    print(max_lcp)