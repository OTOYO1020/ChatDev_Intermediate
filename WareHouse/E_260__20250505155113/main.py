'''
Main application file for the good sequences calculator.
'''
from utils import calculate_good_sequences
def main():
    try:
        M = int(input("Enter M: "))
        N = int(input("Enter N: "))
        pairs = []
        print("Enter pairs (A_i, B_i) separated by commas:")
        for _ in range(N):
            while True:  # Loop until a valid pair is entered
                pair_input = input()
                try:
                    A, B = map(int, pair_input.split(','))
                    if 1 <= A <= M and 1 <= B <= M:
                        pairs.append((A, B))
                        break  # Exit the loop if the pair is valid
                    else:
                        print(f"Invalid pair ({A}, {B}). Both A and B must be between 1 and {M}. Please re-enter.")
                except ValueError:
                    print("Invalid input format. Please enter the pair as two integers separated by a comma.")
        good_sequences = calculate_good_sequences(M, pairs)
        print("Good Sequences:", good_sequences)
    except Exception as e:
        print("Input Error:", str(e))
if __name__ == "__main__":
    main()