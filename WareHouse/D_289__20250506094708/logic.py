'''
Logic file containing the function to determine if the robot can reach the target step.
'''
from collections import deque
def can_reach_step(N, M, A, B, X):  # Ensure X is included as a parameter
    traps = set(B)  # Initialize traps for quick lookup
    queue = deque([0])  # Initialize BFS queue starting from step 0
    visited = set([0])  # Set to track visited steps
    while queue:
        current = queue.popleft()  # Dequeue the current step
        for step_size in A:  # Iterate through each step size in A
            next_step = current + step_size  # Calculate the next step
            if next_step == X:  # Check if the next step is the target
                return "YES"
            if next_step < X and next_step not in traps and next_step not in visited:
                queue.append(next_step)  # Enqueue the next step
                visited.add(next_step)  # Mark the next step as visited
    return "NO"  # Return NO if the target step is not reachable