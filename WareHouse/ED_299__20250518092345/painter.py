'''
Painter class to handle the painting logic based on distance conditions.
'''
from typing import List
class Painter:
    def __init__(self, graph, K: int, p: List[int], d: List[int]):
        self.graph = graph
        self.K = K
        self.p = p
        self.d = d
    def can_paint(self):
        if self.K == 0:
            return True, [1] * self.graph.N  # Paint all vertices black
        all_distances = self.graph.bfs()  # Get distances for all vertices
        for vertex in range(self.graph.N):
            valid = True
            for i in range(min(self.K, len(self.p))):
                if all_distances[vertex][self.p[i]] == -1 or all_distances[vertex][self.p[i]] > self.d[i]:
                    valid = False
                    break
            if valid:
                colors = [0] * self.graph.N
                colors[vertex] = 1  # Paint this vertex black
                return True, colors  # Return immediately if a valid painting is found
        return False, [0] * self.graph.N  # Return unpainted colors if no valid painting is found