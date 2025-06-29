'''
Main application file for the guarded vertices problem.
'''
from collections import deque
from graph import Graph
def main():
    N, M, K = map(int, input().split())
    if M == 0:
        print("No edges to process.")
        return
    edges = []
    for _ in range(M):
        a, b = map(int, input().split())
        if 1 <= a <= N and 1 <= b <= N:  # Validate vertices
            edges.append((a, b))
        else:
            print(f"Invalid edge vertices: {a}, {b}. They must be between 1 and {N}.")
            return
    graph = Graph(N)
    for a, b in edges:
        graph.add_edge(a, b)
    guarded_vertices = set()
    if K == 0:
        print("No guards to process.")
        return
    for _ in range(K):
        position, stamina = map(int, input().split())
        if 1 <= position <= N and stamina >= 0:  # Validate guard position and stamina
            guarded_vertices.update(graph.bfs(position, stamina))
        else:
            print(f"Invalid guard position: {position} or stamina: {stamina}.")
            return
    sorted_guarded = sorted(guarded_vertices)
    print(' '.join(map(str, sorted_guarded)))
if __name__ == "__main__":
    main()