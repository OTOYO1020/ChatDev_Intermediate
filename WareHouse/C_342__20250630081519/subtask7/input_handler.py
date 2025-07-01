'''
Handles input operations for the character replacement application.
'''
class InputHandler:
    def get_operations(self, num_operations, input_lines):
        if len(input_lines) < num_operations:
            raise ValueError(f"Expected {num_operations} operation inputs, but got {len(input_lines)}.")
        operations = []
        for i in range(num_operations):
            try:
                c_i, d_i = input_lines[i].split()
                if len(c_i) != 1 or len(d_i) != 1:
                    raise ValueError(f"Input line {i+1} must contain exactly two characters.")
                operations.append((c_i.strip(), d_i.strip()))
            except ValueError as ve:
                raise ValueError(f"Input line {i+1} is not in the correct format: {ve}")
        return operations