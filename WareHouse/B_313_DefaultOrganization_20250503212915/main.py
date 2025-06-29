'''
Main entry point for the Strongest Programmer application.
'''
from graph import Graph
import sys
class App:
    def __init__(self):
        self.process_input()
    def process_input(self):
        input_data = sys.stdin.read().strip().splitlines()
        try:
            N, M = map(int, input_data[0].split())
            if N < 1:
                raise ValueError("The number of programmers must be at least 1.")
            if len(input_data) < 2 + M:
                raise ValueError("Not enough relations provided.")
            relations = []
            for i in range(1, M + 1):
                A, B = map(int, input_data[i].split())
                if A < 1 or A > N or B < 1 or B > N:
                    raise ValueError("Programmer indices must be between 1 and N.")
                relations.append((A, B))
            graph = Graph(N)
            for A, B in relations:
                graph.add_relation(A - 1, B - 1)  # Adjust for 0-based indexing after validation
            strongest_programmer = graph.find_strongest_programmer()
            print(strongest_programmer)
        except ValueError as e:
            print(f"Error: {str(e)}")
if __name__ == "__main__":
    App()