'''
Handles user input for toy and box sizes.
'''
class InputHandler:
    def get_inputs(self, input_string, is_box=False):
        if not input_string.strip():
            raise ValueError("Input cannot be empty.")
        try:
            sizes = list(map(int, input_string.split(',')))
            if any(size <= 0 for size in sizes):  # Check for positive integers
                raise ValueError("Sizes must be positive integers.")
            if is_box and len(sizes) == 0:
                raise ValueError("Box sizes cannot be empty.")
            return sizes
        except ValueError:
            raise ValueError("Invalid input. Please enter positive integers separated by commas.")