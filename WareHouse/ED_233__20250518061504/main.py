'''
Main application file for the Sum Calculator.
'''
from calculator import calculate_sum
def main():
    '''
    Main function to handle input and output for the sum calculator.
    '''
    try:
        x = int(input("Enter an integer: "))  # Read integer from standard input
        total_sum = calculate_sum(x)
        print(f"Total Sum: {total_sum}")  # Print the result
    except ValueError:
        print("Please enter a valid integer.")
if __name__ == "__main__":
    main()