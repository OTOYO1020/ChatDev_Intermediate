'''
Graph class for managing friendships and blockships.
'''
from collections import defaultdict, deque
class Graph:
    def __init__(self, N):
        self.N = N
        self.friendships = defaultdict(set)
        self.blockships = set()
    def add_friendship(self, A, B):
        self.friendships[A].add(B)
        self.friendships[B].add(A)
    def add_blockship(self, C, D):
        # Add both directions of the blockship relationship
        self.blockships.add((C, D))
        self.blockships.add((D, C))  # Add the reverse relationship
    def is_friendship(self, A, B):
        return B in self.friendships[A]
    def is_blockship(self, A, B):
        return (A, B) in self.blockships or (B, A) in self.blockships
    def bfs(self, start, target):
        visited = set()
        queue = deque([start])
        while queue:
            current = queue.popleft()
            if current == target:
                return True
            visited.add(current)
            for neighbor in self.friendships[current]:
                # Check if the neighbor is not visited
                if neighbor not in visited:
                    # Ensure that moving to this neighbor does not lead to a blocked path to the target
                    if not self.is_blockship(start, neighbor) and not self.is_blockship(neighbor, target):
                        queue.append(neighbor)
        return False