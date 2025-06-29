'''
Main entry point for the Transformation application.
'''
import sys
from transformation import populate_transformation_matrix, calculate_final_element
def main():
    try:
        n = int(input("Enter number of element types (N): "))
        print("Please enter the transformation values for each row, separated by spaces (e.g., '1 2 3 ...'):")
        matrix_values = []
        for _ in range(n):
            while True:
                try:
                    row = list(map(int, input().strip().split()))
                    if len(row) != n:
                        raise ValueError("Each row must contain exactly N values.")
                    if any(value < 1 or value > n for value in row):
                        raise ValueError(f"Each value must be between 1 and {n}.")
                    matrix_values.append(row)
                    break  # Exit the loop if the row is valid
                except ValueError as e:
                    print(f"Input Error: {e}. Please enter the row again using integers only.")
                except Exception as e:
                    print(f"Unexpected Error: {e}. Please enter the row again.")
        # Validate the matrix size
        if len(matrix_values) != n:
            raise ValueError("The number of rows must be equal to N.")
        transformation_matrix = populate_transformation_matrix(n, matrix_values)
        final_element = calculate_final_element(transformation_matrix, n)
        print(f"Final Element: {final_element}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()