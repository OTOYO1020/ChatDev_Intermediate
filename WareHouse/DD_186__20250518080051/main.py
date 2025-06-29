'''
Main entry point of the application that handles user input and output.
'''
from calculator import calculate_sum_of_absolute_differences
def main():
    try:
        # Read input from standard input
        input_data = input("Enter the number of integers followed by the integers separated by spaces: ")
        data = input_data.split()
        # Validate the number of inputs
        if len(data) < 2:
            raise ValueError("You must provide at least one integer after N.")
        N = int(data[0])
        A = []
        # Validate and convert the list of integers
        for num in data[1:]:
            try:
                A.append(int(num))
            except ValueError:
                raise ValueError(f"Invalid integer value: {num}. Please enter valid integers.")
        # Validate the input length
        if len(A) != N:
            raise ValueError("The number of integers provided does not match N.")
        result = calculate_sum_of_absolute_differences(N, A)
        print(f"Sum of Absolute Differences: {result}")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()