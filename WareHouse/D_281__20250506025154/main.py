'''
Main application file for the sum calculator.
'''
from utils import generate_sums, find_max_multiple
def main():
    try:
        N = int(input("Enter N (length of array): "))
        K = int(input("Enter K (number of elements to sum): "))
        if K <= 0:
            print("Error: K must be a positive integer.")
            return
        D = int(input("Enter D (multiple to find): "))
        A_input = input("Enter the sequence of non-negative integers (comma-separated, no spaces): ").strip().split(',')
        # Validate input for A
        if not A_input or A_input == ['']:  # Check for empty input
            raise ValueError("The sequence of integers cannot be empty.")
        A = []
        for num in A_input:
            try:
                value = int(num)
                if value < 0:
                    raise ValueError(f"Invalid entry '{num}': All entries must be non-negative integers.")
                A.append(value)
            except ValueError:
                raise ValueError(f"Invalid entry '{num}': Please enter valid non-negative integers, separated by commas.")
        if len(A) != N:
            raise ValueError("Length of A does not match N.")
        if K > N:
            print("Error: K cannot be greater than N.")
            return
        sums = generate_sums(A, K)
        max_multiple = find_max_multiple(sums, D)
        if max_multiple == -1:
            print("-1")
        else:
            print(f"The maximum multiple of D is: {max_multiple}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()