'''
Handles input operations for the character replacement application.
'''
class InputHandler:
    def get_string(self, input_string):
        return input_string.strip()
    def get_operations(self, num_operations):
        operations = []
        for _ in range(num_operations):
            c_i, d_i = input().split()
            operations.append((c_i.strip(), d_i.strip()))
        return operations