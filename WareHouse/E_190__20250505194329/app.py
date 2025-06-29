'''
Module to define the App class for the console application.
'''
from gem_graph import GemGraph
from gem_manager import GemManager
class App:
    def __init__(self):
        self.graph = GemGraph()
    def run(self):
        while True:
            try:
                # Read integers N and M
                N, M = map(int, input("Enter number of gems (N) and number of edges (M): ").split())
                if N <= 0 or M < 0:
                    raise ValueError("N must be positive and M cannot be negative.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
        # Read M pairs of integers (A_i, B_i)
        print("Enter the edges (A B) one per line:")
        for _ in range(M):
            while True:
                try:
                    a, b = map(int, input().split())
                    if a < 1 or a > N or b < 1 or b > N:
                        raise ValueError(f"Gem types must be between 1 and {N}.")
                    self.graph.add_edge(a, b)
                    break
                except ValueError as e:
                    print(f"Invalid edge input: {e}. Please enter valid integers.")
        # Read integer K and K integers (C_1, C_2, ..., C_K)
        while True:
            try:
                K = int(input("Enter number of required gems (K): "))
                if K <= 0:
                    raise ValueError("K must be positive.")
                required_gems = list(set(map(int, input("Enter the required gems (C1 C2 ...): ").split())))
                if len(required_gems) != K:
                    raise ValueError(f"You must enter exactly {K} unique required gems.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
        manager = GemManager(self.graph)
        found, min_gems = manager.is_possible_and_minimum_gems(required_gems)
        if found:
            result = f"Minimum gems needed: {min_gems}"
        else:
            result = "It is not possible to form the required gem sequence."
        print(result)