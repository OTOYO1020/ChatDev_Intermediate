'''
Main application file for the Bounce Calculator.
'''
from bounce_calculator import parse_input, initialize_variables, calculate_bounce_coordinates, count_valid_bounces, get_result
def main():
    while True:
        try:
            # Read input
            n_str = input("Enter N (number of bounces): ")
            l_str = input("Enter list of integers L (comma-separated): ")
            x_str = input("Enter X (maximum coordinate): ")
            # Use the parse_input function from the bounce_calculator module
            N, L, X = parse_input(n_str, l_str, x_str)
            # Calculate bounce coordinates
            D = calculate_bounce_coordinates(N, L)
            # Count valid bounces
            count = count_valid_bounces(D, X)
            # Get and print the result
            result = get_result(count)  # Call get_result to format the output
            print(result)
            break  # Exit the loop if everything is successful
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
if __name__ == "__main__":
    main()