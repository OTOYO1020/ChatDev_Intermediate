'''
Main application file for the Bounce Calculator.
'''
from bounce_calculator import parse_input, initialize_variables, calculate_bounce_coordinates, count_valid_bounces, get_result
def main():
    input_string = input("Enter N, L (comma-separated), and X: ")
    try:
        N, L, X = parse_input(input_string)
        D = initialize_variables()  # Initialize D with only the first element
        calculate_bounce_coordinates(N, L, D)
        result = get_result(D, X)  # Pass D and X to get_result
        print(f"Valid Bounces: {result}")
    except Exception as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()