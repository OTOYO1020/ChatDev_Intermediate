'''
Module to define the App class for the command-line application.
'''
from typing import List, Tuple
from rope_graph import RopeGraph
class App:
    def __init__(self):
        self.graph = None
    def run(self):
        try:
            N = int(input("Enter the number of ropes (N): "))
            M = int(input("Enter the number of operations (M): "))
        except ValueError:
            print("Invalid input. Please enter integers for N and M.")
            return
        if M == 0:
            print(f"Number of cycles: 0, Number of non-cycles: {N}")
            return
        self.graph = RopeGraph(N)
        for _ in range(M):
            operation = input("Enter operation (end1 color1 end2 color2): ")
            try:
                end1, color1, end2, color2 = operation.split()
                self.graph.tie_ends(int(end1), color1, int(end2), color2)
            except ValueError:
                print("Invalid operation format. Please enter in the format: end1 color1 end2 color2.")
                continue
        cycles, non_cycles = self.graph.count_cycles_and_non_cycles()
        print(f"Number of cycles: {cycles}, Number of non-cycles: {non_cycles}")