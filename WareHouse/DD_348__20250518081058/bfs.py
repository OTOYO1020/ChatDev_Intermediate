'''
Module that contains the BFS algorithm to determine if the goal can be reached.
'''
from collections import deque
from typing import List, Tuple
def canReachGoal(H: int, W: int, grid: List[List[str]], medicines: List[Tuple[int, int, int]], start: Tuple[int, int], goal: Tuple[int, int]) -> bool:
    energy = 0
    # BFS initialization
    queue = deque([(start[0], start[1], energy)])  # (row, col, current_energy)
    visited = {}  # Dictionary to track maximum energy levels at each cell
    visited[start] = energy
    medicine_set = {(m[0], m[1]): m[2] for m in medicines}  # Set for quick lookup of medicines
    while queue:
        r, c, current_energy = queue.popleft()
        # Check if we reached the goal
        if (r, c) == goal:
            return True
        # Explore neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != '#':
                new_energy = current_energy
                # Check if the cell is a medicine cell
                if (nr, nc) in medicine_set:
                    new_energy += medicine_set[(nr, nc)]  # Update energy with medicine value
                # Only add to queue if we have not visited this cell with a higher energy level
                if (nr, nc) not in visited or visited[(nr, nc)] < new_energy:
                    visited[(nr, nc)] = new_energy
                    queue.append((nr, nc, new_energy))  # Add new state to the queue
    return False