'''
Main application file for the Takahashi Score Calculator.
'''
import sys
from score_calculator import calculate_score
def main():
    # Read the integer N from standard input
    try:
        N = int(input().strip())
        if N <= 0:
            raise ValueError("N must be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid positive integer for N.")
        sys.exit(1)
    # Read the grades from standard input
    while True:
        grades_input = input(f"Please enter exactly {5 * N} grades separated by spaces (e.g., '85 90 78 92 88'): ").strip()
        if not grades_input:  # Check for empty input
            print("Error: Input cannot be empty. Please enter the grades.")
            continue
        try:
            grades = list(map(int, grades_input.split()))
            # Check for negative grades
            if any(grade < 0 for grade in grades):
                raise ValueError("Grades must be non-negative integers.")
        except ValueError as e:
            print(f"Error: {e}. Please enter valid integers for grades, separated by spaces.")
            continue
        except Exception as e:
            print(f"Error: Invalid input detected. Please ensure all grades are integers. {e}")
            continue
        if len(grades) != 5 * N:
            print(f"Error: The number of grades must be {5 * N}. You entered {len(grades)} grades.")
            continue
        break  # Exit the loop if all validations are passed
    # Calculate the score
    score = calculate_score(N, grades)
    # Print the score formatted to a floating-point number
    print(f"{score:.2f}")
if __name__ == "__main__":
    main()