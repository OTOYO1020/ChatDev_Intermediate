'''
Module to handle user input for the grid size and black pawns.
'''
import re  # Import the regular expression module
class InputHandler:
    def get_input(self):
        N = int(input("Enter grid size (N): "))
        M = int(input("Enter number of black pawns (M): "))
        black_pawns = set()  # Use a set to avoid duplicates
        for _ in range(M):
            while True:
                try:
                    position_input = input("Enter black pawn position (X,Y): ").strip()
                    # Validate the input format using regex
                    if not re.match(r'^\d+,\d+$', position_input):
                        raise ValueError("Invalid input format. Please enter the position as 'X,Y' where X and Y are integers.")
                    x, y = map(int, position_input.split(','))
                    if (x, y) in black_pawns:  # Check for duplicates before adding
                        raise ValueError(f"Duplicate black pawn position ({x}, {y}) detected.")
                    black_pawns.add((x, y))  # Add to set to avoid duplicates
                    break  # Exit the loop if input is valid
                except ValueError as e:
                    print(e)  # Print the error message
        self.validate_input(N, M, black_pawns)
        return N, M, list(black_pawns)  # Convert back to list for compatibility
    def validate_input(self, N, M, black_pawns):
        # Validate the input values
        if N <= 0:
            raise ValueError("Grid size must be a positive integer.")
        if M < 0:
            raise ValueError("Number of black pawns cannot be negative.")
        for x, y in black_pawns:
            if x < 0 or y < 0 or x > 2 * N or y > 2 * N:
                raise ValueError(f"Black pawn position ({x}, {y}) is out of bounds.")