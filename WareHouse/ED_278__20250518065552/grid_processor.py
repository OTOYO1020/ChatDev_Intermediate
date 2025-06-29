'''
Grid processor module for counting distinct integers outside blackout areas.
'''
from typing import List
class GridProcessor:
    def count_distinct_integers(self, H: int, W: int, N: int, A: List[List[int]], h: int, w: int) -> List[int]:
        # Input validation
        if H <= 0 or W <= 0 or N <= 0 or h <= 0 or w <= 0:
            raise ValueError("Height (H), Width (W), Number of Rows (N), Blackout Height (h), and Blackout Width (w) must be positive integers.")
        if len(A) != N or any(len(row) != W for row in A):
            raise ValueError("Grid dimensions do not match specified height and width.")
        if h > H or w > W:
            raise ValueError("Blackout dimensions cannot exceed grid dimensions.")
        results = []
        for k in range(H - h + 1):
            for l in range(W - w + 1):
                distinct_integers = set()
                # Iterate only over the relevant portion of the grid
                for i in range(H):
                    for j in range(W):
                        if i < k or i >= k + h or j < l or j >= l + w:
                            distinct_integers.add(A[i][j])
                results.append(len(distinct_integers))
        return results