'''
Main application file for the Contest Rating application.
'''
from rating_calculator import max_rating
def main():
    try:
        # Read input from standard input
        input_data = input("Enter the number of contests followed by performances (comma-separated, e.g., '3,10,20,30'): ")
        input_list = list(map(str.strip, input_data.split(',')))  # Strip whitespace
        N = int(input_list[0])  # Convert to integer
        performances = list(map(int, input_list[1:]))  # Convert the rest to integers
        if len(performances) != N:
            raise ValueError("The number of performances must match N.")
        max_rating_value = max_rating(N, performances)
        print(f"Maximum Rating: {max_rating_value:.2f}")
    except ValueError as e:
        print(f"Input Error: {e}. Please ensure you enter a valid number of contests followed by their performances.")
    except Exception as e:
        print(f"Unexpected Error: {e}. Please check your input format.")
if __name__ == "__main__":
    main()