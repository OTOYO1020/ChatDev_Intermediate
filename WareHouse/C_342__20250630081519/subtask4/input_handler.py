'''
Handles input operations for the character replacement application.
'''
class InputHandler:
    def get_string(self, input_string):
        return input_string.strip()
    def get_operations(self, num_operations, input_lines):
        operations = []
        for i in range(num_operations):
            try:
                c_i, d_i = input_lines[i].split()
                operations.append((c_i.strip(), d_i.strip()))
            except ValueError:
                raise ValueError(f"Input line {i+1} is not in the correct format. Expected two characters.")
        return operations