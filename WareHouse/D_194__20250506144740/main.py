'''
Main application file that initializes and runs the Graph Connectivity Calculator.
'''
def calculate_operations(N):
    """
    Calculate the expected number of operations needed for a graph with N vertices to become connected.
    Parameters:
    N (int): The number of vertices in the graph.
    Returns:
    float: The expected number of operations rounded to six decimal places.
    """
    if N <= 0:
        raise ValueError("N must be a positive integer.")
    if N == 1:
        return 0.0  # If there's only one vertex, no operations are needed.
    expected_operations = 0
    connected_components = N
    while connected_components > 1:
        p = (connected_components - 1) / N
        expected_operations += 1 / (1 - p)
        connected_components -= 1
    return round(expected_operations, 6)
if __name__ == "__main__":
    try:
        N = int(input("Enter the number of vertices (N): "))
        result = calculate_operations(N)
        print("Expected Operations:", result)
    except ValueError as e:
        print("Invalid input. Please enter a valid integer.", e)