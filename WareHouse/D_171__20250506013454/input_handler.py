'''
Handles user input for the sequence and operations.
'''
class InputHandler:
    def get_operations(self, num_operations):
        operations = []
        for _ in range(num_operations):
            b, c = map(int, input("Enter B and C (space-separated): ").strip().split())
            operations.append((b, c))
        return operations