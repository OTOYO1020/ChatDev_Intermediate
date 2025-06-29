'''
Handles user input and validation.
'''
class InputHandler:
    def __init__(self):
        pass
    def validate_input(self, n, d, sequence):
        if not isinstance(n, int) or not isinstance(d, int):
            return False
        if n <= 0:
            return False
        # Check if all elements in sequence can be converted to integers
        for item in sequence:
            item = item.strip()  # Trim whitespace
            if not item:  # Check for empty strings
                return False
            try:
                int_value = int(item)  # Attempt to convert to integer
                # Optional: Check for specific range if needed
                if int_value < 0:  # Example condition
                    return False
            except ValueError:
                return False
        return True