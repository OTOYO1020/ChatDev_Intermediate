'''
Main entry point of the application that runs the cycle detection.
'''
from graph_cycle_detector import GraphCycleDetector
from input_validation import InputValidation
def main():
    N = int(input("Enter number of vertices (N): "))
    M = int(input("Enter number of edges (M): "))
    edges_input = input("Enter edges (comma-separated tuples, e.g., (1,2),(2,3)): ")
    # Validate edges input format
    if not edges_input.strip():
        print("Edges input cannot be empty.")
        return
    edges = []
    try:
        for edge in edges_input.split(','):
            edge = edge.strip().strip('()')
            u, v = map(int, edge.split(','))
            edges.append((u, v))
    except ValueError:
        print("Invalid edges format. Please enter edges as comma-separated tuples.")
        return
    # Check if the number of edges matches M
    if len(edges) != M:
        print(f"Error: The number of edges provided ({len(edges)}) does not match M ({M}).")
        return
    # Validate input
    validator = InputValidation()
    if not validator.validate_input(N, M, edges):
        print("Invalid input parameters.")
        return
    # Run cycle detection
    detector = GraphCycleDetector(N, M, edges)
    result = detector.find_cycle()
    if result is not None:
        print(f"Minimum edges in cycle containing vertex 1: {result}")
    else:
        print("No cycle found containing vertex 1.")
if __name__ == "__main__":
    main()