'''
Main application file for the robot coordinate calculator.
'''
from coordinate_calculator import greatest_coordinate
def main():
    '''
    Main function to handle input and output for the robot coordinate calculator.
    '''
    try:
        n = int(input("Enter the length of the sequence (0 for no movements): "))
        if n < 0:
            raise ValueError("Length of sequence cannot be negative.")
        if n == 0:
            print("Greatest Coordinate: 0")
            return  # Exit the function early if no movements
        sequence_input = input("Enter the sequence of integers (space-separated): ").split()
        # Validate that all inputs are integers
        sequence = []
        for item in sequence_input:
            try:
                sequence.append(int(item))
            except ValueError:
                raise ValueError(f"Invalid input '{item}': Please enter only integers.")
        if len(sequence) != n:
            raise ValueError("Length of sequence does not match the specified length.")
        result = greatest_coordinate(sequence)
        print(f"Greatest Coordinate: {result}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()