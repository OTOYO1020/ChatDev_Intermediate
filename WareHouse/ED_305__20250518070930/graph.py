'''
Contains the Graph class and the function to find guarded vertices.
'''
from collections import deque
from typing import List, Tuple, Set
class Graph:
    def __init__(self, N: int, edges: List[Tuple[int, int]]):
        '''
        Initializes the graph with N vertices and the given edges.
        '''
        self.adjacency_list = {i: [] for i in range(N)}
        for u, v in edges:
            self.adjacency_list[u].append(v)
            self.adjacency_list[v].append(u)
    def bfs(self, start: int, stamina: int) -> Set[int]:
        '''
        Performs a breadth-first search to find all vertices within the stamina range of the guard.
        Parameters:
        start (int): The starting vertex for the BFS.
        stamina (int): The stamina of the guard.
        Returns:
        Set[int]: A set of vertices that are guarded by the guard.
        '''
        if stamina == 0:
            return {start}  # Guard only guards their own position if stamina is zero
        visited = set()
        queue = deque([(start, 0)])  # (current_vertex, current_distance)
        guarded_vertices = set()
        while queue:
            current, distance = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            if distance <= stamina:
                guarded_vertices.add(current)
            for neighbor in self.adjacency_list[current]:
                if neighbor not in visited:  # Check before adding to the queue
                    queue.append((neighbor, distance + 1))
        return guarded_vertices
def find_guarded_vertices(N: int, M: int, edges: List[Tuple[int, int]], K: int, guards: List[Tuple[int, int]]) -> List[int]:
    '''
    Finds all unique guarded vertices based on the positions and stamina of the guards.
    Parameters:
    N (int): The number of vertices.
    M (int): The number of edges.
    edges (List[Tuple[int, int]]): The list of edges in the graph.
    K (int): The number of guards.
    guards (List[Tuple[int, int]]): The list of guards with their positions and stamina.
    Returns:
    List[int]: A sorted list of unique guarded vertices.
    '''
    if K != len(guards):
        raise ValueError(f"The number of guards provided ({len(guards)}) does not match K ({K}).")
    if K == 0 or not guards:  # No guards, no guarded vertices
        return []
    if M == 0 or not edges:  # No edges, no guarded vertices can be guarded
        return []
    graph = Graph(N, edges)
    guarded_vertices = set()
    for guard in guards:
        position, stamina = guard
        guarded_vertices.update(graph.bfs(position, stamina))
    return sorted(guarded_vertices)