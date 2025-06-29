'''
Handles input reception and parsing for the application.
'''
class InputHandler:
    def __init__(self, input_text, n):
        self.input_text = input_text
        self.n = n  # Store N for validation
    def get_input(self):
        constraints = []
        lines = self.input_text.strip().splitlines()
        for line in lines:
            try:
                x, y, z = map(int, line.split())
                if x < 1 or x > self.n or y < 1 or y > self.n:  # Use self.n
                    raise ValueError("X and Y must be within the range of 1 to N.")
                constraints.append((x - 1, y - 1, z % 2))  # Convert to 0-based index and mod 2
            except ValueError:
                raise ValueError("Each constraint must consist of three integers (X Y Z). Please check your input.")
            except Exception as e:
                raise Exception(f"An error occurred while processing the input: {str(e)}")
        return constraints