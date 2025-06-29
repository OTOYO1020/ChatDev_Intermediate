'''
Main entry point for the application.
'''
def main():
    import sys
    from graph import Graph
    # Read input from standard input
    input_data = sys.stdin.read().strip().splitlines()
    N = int(input_data[0])
    M = int(input_data[1])
    a = list(map(int, input_data[2].split())) if M > 0 else []
    # Input validation
    if N <= 0 or M < 0:
        raise ValueError("N must be a positive integer and M must be a non-negative integer.")
    if any(x < 1 or x > N for x in a):
        raise ValueError("All elements in array a must be between 1 and N.")
    # Initialize the graph
    graph = Graph(N)
    # Add edges based on the array a
    if M > 0:
        for i in range(M - 1):  # Iterate through the original array
            graph.add_edge(a[i], a[i + 1])  # Add an edge between consecutive elements
    # Handle case when M is 0
    if M == 0:
        order = list(range(N, 0, -1))
        print(" ".join(map(str, order)))
        return
    unread = set(range(1, N + 1))
    order = []
    while unread:
        x = min(unread)
        component = graph.get_connected_component(x)
        order.extend(sorted(component, reverse=True))
        unread.difference_update(component)
    result = " ".join(map(str, order))
    print(result)
if __name__ == "__main__":
    main()