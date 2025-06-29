'''
Main application file for the SumGreaterApp.
'''
from utils import calculate_sums
def main():
    '''
    Main function to read input and calculate sums of greater elements.
    '''
    try:
        # Read the length of the sequence
        N = int(input("Enter the length of the sequence (positive integer): "))
        # Handle case where N is 0 or negative
        if N <= 0:
            print("The sequence must have at least one element. Exiting.")
            return
        while True:
            # Read the sequence of integers
            input_text = input(f"Enter {N} integers (space-separated): ")
            try:
                sequence = list(map(int, input_text.split()))
                if len(sequence) == N:
                    break
                else:
                    print(f"Error: Please enter exactly {N} integers.")
            except ValueError:
                print("Error: Please enter valid integers.")
        result = calculate_sums(sequence)
        print("Result:", result)
    except ValueError as e:
        print("Input Error:", e)
if __name__ == "__main__":
    main()