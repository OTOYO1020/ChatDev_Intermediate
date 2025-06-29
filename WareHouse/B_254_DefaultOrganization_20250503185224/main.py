'''
Main application file for generating and displaying integer sequences using standard input and output.
'''
from sequence_generator import SequenceGenerator
def main():
    try:
        N = int(input("Please enter an integer N within the range 1 to 30: "))
        if N < 1 or N > 30:
            raise ValueError("N must be between 1 and 30.")
        generator = SequenceGenerator(N)
        sequences = generator.generate()
        display_sequences(sequences)
    except ValueError as e:
        print(f"Input Error: {str(e)}")
def display_sequences(sequences):
    for seq in sequences:
        print(' '.join(map(str, seq)))
if __name__ == "__main__":
    main()