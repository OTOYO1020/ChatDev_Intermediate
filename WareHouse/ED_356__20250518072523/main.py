'''
Main file to run the Sum Calculator application.
'''
from sum_calculator import calculate_sum
def main():
    try:
        N = int(input("Enter the number of elements (N): "))
        if N <= 0:
            print("Result: 0")
            return  # Early exit for N <= 0
        A_input = input("Enter the list of integers (space-separated): ").split()
        # Validate the length of A
        if len(A_input) != N:
            raise ValueError("Length of A must be equal to N.")
        # Validate that all elements in A are integers
        A = []
        for num in A_input:
            try:
                A.append(int(num))
            except ValueError:
                print(f"Invalid input '{num}': All elements must be integers.")
                return  # Exit if invalid input is found
        total_sum = calculate_sum(N, A)
        print("Result:", total_sum)
    except ValueError as ve:
        print("Input Error:", str(ve))
    except Exception as e:
        print("Error:", str(e))
if __name__ == "__main__":
    main()