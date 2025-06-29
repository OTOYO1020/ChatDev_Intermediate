'''
Module for calculating minimum operations to reach N from 1 using a.
'''
from collections import deque
def min_operations(a: int, N: int) -> int:
    '''
    Calculate the minimum operations needed to reach N from 1 using multiplication by a
    and string manipulation.
    '''
    x = 1
    operations_count = 0
    visited = set()  # To avoid infinite loops by tracking visited states
    queue = deque([(x, operations_count)])  # Initialize queue with the starting value
    while queue:
        current_x, current_operations_count = queue.popleft()
        # Check if we have reached N
        if current_x == N:
            return current_operations_count
        # Skip processing if current_x exceeds N
        if current_x > N:
            continue
        # Check multiplication operation
        new_x = current_x * a
        if new_x <= N and new_x not in visited:
            visited.add(new_x)
            queue.append((new_x, current_operations_count + 1))
        # Check string manipulation operation
        if current_x >= 10 and current_x % 10 != 0:
            x_str = str(current_x)
            new_x = int(x_str[-1] + x_str[:-1])  # Move last character to front
            if new_x <= N and new_x not in visited:  # Check if new_x is within bounds
                visited.add(new_x)
                queue.append((new_x, current_operations_count + 1))
    return -1  # If no valid operations can lead to N