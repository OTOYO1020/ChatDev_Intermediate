'''
Contains the InputFrame class for user input.
'''
import sys
class InputFrame:
    def __init__(self):
        self.n = self.get_positive_integer("Number of Cards (N): ")
        self.m = self.get_positive_integer("Number of Operations (M): ")
        self.a = self.get_integer_list("Initial Card Values (A): ", self.n)
        self.operations = []
        for _ in range(self.m):
            b, c = self.get_operation_input()
            self.operations.append((b, c))
    def get_input(self):
        return self.n, self.m, self.a, self.operations
    def get_positive_integer(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    def get_integer_list(self, prompt, expected_length):
        while True:
            try:
                values = list(map(int, input(prompt).split()))
                if len(values) == expected_length:
                    return values
                else:
                    print(f"Please enter exactly {expected_length} integers.")
            except ValueError:
                print("Invalid input. Please enter valid integers.")
    def get_operation_input(self):
        while True:
            try:
                b, c = map(int, input("Operations (B_j, C_j): ").split())
                if 0 < b <= self.n:  # Ensure B_j is a positive integer and does not exceed N
                    return b, c
                else:
                    print("B_j must be a positive integer and cannot exceed the number of cards (N).")
            except ValueError:
                print("Invalid input. Please enter valid integers for B_j and C_j.")