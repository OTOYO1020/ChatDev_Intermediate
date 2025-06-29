'''
Main application file for the string manipulation.
'''
from utils import validate_input
def main():
    # Read input from standard input
    while True:
        l = input("Enter L (positive integer): ")
        r = input("Enter R (positive integer): ")
        s = input("Enter String S: ")
        if validate_input(l, r, s):
            break  # Exit the loop if input is valid
        else:
            print("Please try again.")
    l = int(l) - 1  # Convert to zero-based index
    r = int(r) - 1  # Convert to zero-based index
    # Extract and reverse the substring
    substring = s[l:r + 1][::-1]
    result = s[:l] + substring + s[r + 1:]
    # Print the result
    print(result)
if __name__ == "__main__":
    main()