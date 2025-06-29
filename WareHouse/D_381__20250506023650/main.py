'''
Main application file for the 1122 sequence finder.
'''
from helpers import find_max_length_1122_sequence
def main():
    '''
    Main function to read input and calculate the maximum length of the 1122 sequence.
    '''
    input_text = input("Enter the sequence of positive integers (space-separated): ")
    try:
        sequence = list(map(int, input_text.split()))
        max_length = find_max_length_1122_sequence(sequence)
        print(f"Max Length of 1122 Sequence: {max_length}")
    except ValueError:
        print("Please enter a valid sequence of integers.")
if __name__ == "__main__":
    main()