'''
Main application file for the Amoeba Generation Distance Calculator.
'''
import sys
from collections import deque
class MainApp:
    def __init__(self):
        self.parent = []
        self.generations = []
    def read_input(self):
        while True:
            try:
                N = int(input("Enter the number of records: "))
                if N < 1:
                    raise ValueError("N must be a positive integer.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
        self.parent = [0] * (2 * N + 2)
        self.generations = [0] * (2 * N + 2)
        self.parent[1] = 0  # Amoeba 1 has no parent
        for i in range(1, N + 1):
            attempts = 0
            while attempts < 3:  # Allow up to 3 attempts
                try:
                    A_i = int(input(f"Please enter the parent amoeba for amoeba {i} (valid range: 1 to {N}): "))
                    if A_i < 1 or A_i > N:
                        raise ValueError(f"Amoeba {A_i} is out of valid range (1 to {N}).")
                    break
                except ValueError as e:
                    attempts += 1
                    print(f"Invalid input: {e}. Please try again.")
                    if attempts == 3:
                        print("Too many invalid attempts. Please restart the program.")
                        return  # Instead of exiting, allow the user to restart
            self.parent[2 * i] = A_i
            self.parent[2 * i + 1] = A_i
    def calculate_generation_distances(self):
        self.generations[1] = 0
        queue = deque([1])  # Using deque for efficient queue operations
        while queue:
            current = queue.popleft()
            for child in (2 * current, 2 * current + 1):
                # Check if child exists, is within the valid range, and has a parent
                if 0 < child < len(self.generations) and self.parent[child] != 0:
                    self.generations[child] = self.generations[current] + 1
                    queue.append(child)
    def display_results(self):
        # Output only the generation distances for valid amoebae from 1 to 2N + 1
        print(" ".join(map(str, self.generations[1:2 * len(self.generations) // 2 + 1])))
if __name__ == "__main__":
    app = MainApp()
    app.read_input()
    app.calculate_generation_distances()
    app.display_results()