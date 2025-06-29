'''
Main entry point for the graph simulator application.
'''
from graph_simulator import GraphSimulator
if __name__ == "__main__":
    N = int(input("Enter number of vertices (N): "))
    if N <= 0:
        raise ValueError("N must be a positive integer.")
    simulator = GraphSimulator()
    result = simulator.expected_operations(N)
    print(f"Expected Operations: {result:.2f}")