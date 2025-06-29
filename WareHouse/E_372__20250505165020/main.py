'''
Main entry point for the graph application.
'''
from graph import Graph
def main():
    # Read integers N and Q from standard input
    N, Q = map(int, input().split())
    graph = Graph(N)
    results = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        query_type = query[0]
        if query_type == 1:  # Add edge
            u, v = query[1], query[2]
            if not graph.add_edge(u, v):
                print(f"Failed to add edge between {u} and {v}.")
        elif query_type == 2:  # Find k-th largest
            v, k = query[1], query[2]
            result = graph.find_kth_largest(v, k)
            results.append(result)
    # Print results for all Type 2 queries
    for res in results:
        print(res)
if __name__ == "__main__":
    main()