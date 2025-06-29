'''
Main application file for counting valid integer sequences.
'''
from sequence_counter import count_sequences
from input_validation import validate_input
def main():
    try:
        N = input("Enter N (length of sequences, must be a positive integer): ")
        M = input("Enter M (maximum value in sequences, must be a positive integer): ")
        K = input("Enter K (maximum sum of sequences, must be a non-negative integer): ")
        if validate_input(N, M, K):
            result = count_sequences(int(N), int(M), int(K))
            print(f"Valid sequences count: {result}")
        else:
            print("Input Error: Please enter valid positive integers.")
    except ValueError:
        print("Input Error: Please enter valid integers.")
if __name__ == "__main__":
    main()