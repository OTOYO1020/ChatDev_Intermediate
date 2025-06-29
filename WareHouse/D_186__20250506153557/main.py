'''
Main application file for the absolute difference calculator.
'''
from utils import calculate_total_sum
def main():
    try:
        n = int(input("Enter the number of integers (N): "))
        if n < 1:
            raise ValueError("N must be a positive integer.")
        array_input = input("Enter the integers separated by spaces: ")
        array = []
        # Improved input validation for array elements
        for item in array_input.split():
            try:
                array.append(int(item))
            except ValueError:
                raise ValueError(f"'{item}' is not a valid integer.")
        if len(array) != n:
            raise ValueError("The number of integers does not match N.")
        total_sum = calculate_total_sum(array)
        print(f"Total Sum of Absolute Differences: {total_sum}")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()