'''
Main application file for the Majority Operation.
'''
from majority import majority_operation, calculate_min_changes
def main():
    try:
        n = int(input("Enter N (1-13): "))
        if n < 1 or n > 13:
            raise ValueError("N must be between 1 and 13.")
        a = input("Enter binary string A: ")
        if len(a) != 3**n or not all(c in '01' for c in a):
            raise ValueError("Binary string A must be of length 3^N and consist of '0' and '1'.")
        current_string = a
        for _ in range(n):
            current_string = majority_operation(current_string)
        target = '1' if current_string == '0' else '0'
        min_changes = calculate_min_changes(a, target)
        print(f"Minimum changes required: {min_changes}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()