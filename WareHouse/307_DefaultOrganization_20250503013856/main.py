'''
Main application file for the Palindrome Checker.
'''
from palindrome_checker import is_palindrome
def main():
    N = int(input("Enter the number of distinct strings: "))  # Read the number of strings
    strings = []  # Initialize an empty list to store distinct strings
    while len(strings) < N:
        input_string = input(f"Enter string {len(strings) + 1}: ")  # Prompt for each string
        if input_string in strings:
            print("Error: Please enter a distinct string.")  # Inform user of duplicate
        else:
            strings.append(input_string)  # Add to list if distinct
    # Use nested loops to iterate over all pairs of distinct indices
    for i in range(N):
        for j in range(N):  # Iterate over all indices
            if i != j:  # Ensure i and j are distinct
                concat_str1 = strings[i] + strings[j]  # Concatenate strings
                if is_palindrome(concat_str1):
                    print("YES")  # Output YES if a palindrome is found
                    return  # Exit the program after finding a palindrome
    print("NO")  # Output NO if no palindrome is found
if __name__ == "__main__":
    main()