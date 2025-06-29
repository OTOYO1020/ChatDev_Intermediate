'''
Main entry point for the String Manipulator application.
'''
from typing import List, Tuple
from string_operations import StringOperations  # Import the StringOperations class
def main():
    # Read the input string S
    S = input("Enter the string S: ")
    if not S:  # Check for empty string
        print("The input string cannot be empty.")
        return
    N = len(S)  # Length of the string
    try:
        Q = int(input("Enter the number of operations Q: "))  # Read the number of operations
    except ValueError:
        print("Invalid input for number of operations. Please enter an integer.")
        return  # Exit the program if Q is not valid
    if Q <= 0:
        print("Number of operations must be greater than zero.")
        return  # Exit the program if Q is not valid
    operations = []
    print("Please enter each operation as two characters separated by a space (e.g., 'a b' to replace 'a' with 'b'):")
    for _ in range(Q):
        while True:  # Loop until a valid operation is entered
            operation = input().strip().split()
            if len(operation) == 2 and len(operation[0]) == 1 and len(operation[1]) == 1:
                operations.append((operation[0], operation[1]))  # Append the operation as a tuple
                break  # Exit the loop if the operation is valid
            else:
                print("Invalid operation format. Please enter two single characters separated by a space.")
    # Use the StringOperations class to perform operations
    string_operations = StringOperations(S, operations)
    result = string_operations.perform_operations()
    print("Result:", result)
if __name__ == "__main__":
    main()