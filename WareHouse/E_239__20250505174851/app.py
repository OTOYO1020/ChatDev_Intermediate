'''
Module to define the application for querying the tree.
'''
from tree import Tree
class App:
    def __init__(self):
        self.tree = Tree()
    def read_input(self):
        # Read N and Q with validation
        while True:
            try:
                N, Q = map(int, input("Enter number of vertices (N) and number of queries (Q): ").split())
                if N <= 1 or Q < 0:
                    raise ValueError("N must be greater than 1 and Q must be non-negative.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
        # Read values for vertices
        while True:
            try:
                values = list(map(int, input(f"Enter {N} vertex values (space-separated): ").split()))
                if len(values) != N:
                    raise ValueError(f"You must enter exactly {N} values.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
        for i in range(1, N + 1):  # Assuming vertices are 1-indexed
            self.tree.set_value(i, values[i - 1])
        # Handle case for N = 1
        if N == 1:
            print("Tree has only one vertex. No edges to input.")
            print(f"Enter {Q} queries (vertex k):")
            results = []
            for _ in range(Q):
                while True:
                    try:
                        vertex, k = map(int, input().split())
                        if vertex != 1 or k < 1:
                            raise ValueError("Vertex must be 1 and K must be positive.")
                        result = self.tree.find_kth_largest(vertex, k)
                        if result is None:
                            print(f"K is greater than the number of values in the subtree.")
                        else:
                            results.append(result)
                        break
                    except ValueError as e:
                        print(f"Invalid input: {e}. Please try again.")
                    except Exception as e:
                        print(f"Error occurred: {e}. Please try again.")
            # Print results for all queries
            for res in results:
                print(res)
            return  # Exit after handling single vertex case
        # Read edges with validation
        print(f"Enter {N-1} edges (parent child) for the tree (1-indexed):")
        for _ in range(N - 1):
            while True:
                try:
                    parent, child = map(int, input().split())
                    if parent < 1 or parent > N or child < 1 or child > N:
                        raise ValueError("Parent and child must be within the range of vertices.")
                    self.tree.add_edge(parent, child)
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please try again.")
        # Process queries with validation
        print(f"Enter {Q} queries (vertex k):")
        results = []
        for _ in range(Q):
            while True:
                try:
                    vertex, k = map(int, input().split())
                    if vertex < 1 or vertex > N or k < 1:
                        raise ValueError("Vertex must be within the range of vertices and K must be positive.")
                    result = self.tree.find_kth_largest(vertex, k)
                    if result is None:
                        print(f"K is greater than the number of values in the subtree.")
                    else:
                        results.append(result)
                    break
                except ValueError as e:
                    print(f"Error: {e}. Please try again.")
                except Exception as e:
                    print(f"Error occurred: {e}. Please try again.")
        # Print results for all queries
        for res in results:
            print(res)
    def run(self):
        self.read_input()  # Start the application logic