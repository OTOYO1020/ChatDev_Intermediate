'''
Main application file for the integer reduction program using standard input and output.
'''
from operations import reduce_value, calculate_operations
def main():
    try:
        N = int(input("Enter the number of integers: "))
        if N <= 0:
            print("Please enter a positive integer for N.")
            return
        input_text = input("Enter integers separated by spaces: ")
        numbers = list(map(int, input_text.split()))
        if len(numbers) != N:
            print("The number of integers provided does not match N.")
            return
        total_operations = calculate_operations(numbers)
        if total_operations == -1:
            print("Cannot reduce to a common value.")
        else:
            print(f"Total operations: {total_operations}")
    except ValueError:
        print("Please enter valid integers.")
if __name__ == "__main__":
    main()