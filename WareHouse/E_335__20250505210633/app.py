'''
Module to create the console application for user interaction.
'''
from graph import Graph
from dfs import DFS
class App:
    def run(self):
        # Read number of vertices and edges
        while True:
            try:
                N, M = map(int, input("Enter number of vertices and edges (N M): ").split())
                if N <= 0 or M < 0:
                    raise ValueError("N must be positive and M cannot be negative.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter valid integers.")
        graph = Graph(N)
        # Check if M is zero
        if M == 0:
            print("No edges to read.")
        else:
            # Read edges
            print("Enter edges (u v) one per line:")
            for _ in range(M):
                while True:
                    try:
                        u, v = map(int, input().split())
                        if u < 1 or u > N or v < 1 or v > N:
                            raise ValueError("Vertices must be between 1 and N.")
                        graph.add_edge(u, v)
                        break
                    except ValueError as e:
                        print(f"Invalid edge input: {e}. Please enter valid integers.")
        # Read values at vertices
        while True:
            try:
                A = list(map(int, input("Enter values at vertices (space-separated): ").split()))
                if len(A) != N:
                    raise ValueError(f"Must provide exactly {N} values.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter valid integers.")
        # Perform DFS and calculate max score
        dfs = DFS(graph, A)
        max_score = dfs.find_max_score()
        # Output the result
        print(f"Maximum Score: {max_score}")