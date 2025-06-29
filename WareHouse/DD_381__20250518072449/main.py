'''
Main application file for the 1122 sequence finder.
'''
from utils import max_1122_subarray_length
def main():
    '''
    Main function to handle input and output for the 1122 sequence finder.
    '''
    input_text = input("Enter a list of positive integers (comma-separated): ")
    try:
        # Convert input string to a list of integers
        A = list(map(int, input_text.split(',')))
        max_length = max_1122_subarray_length(A)
        print(f"Maximum Length of 1122 Sequence: {max_length}")
    except ValueError:
        print("Please enter a valid list of integers.")
if __name__ == "__main__":
    main()