'''
Simulation logic for calculating the final positions of children.
'''
def simulate_children(movement_string):
    '''
    Simulates the movement of children based on the input string.
    Args:
        movement_string (str): A string consisting of 'L' and 'R'.
    Returns:
        list: A list containing the count of children on each square.
    '''
    N = len(movement_string)
    children_count = [1] * N  # Initialize with 1 child on each square
    current_position = 0  # Start at the leftmost square
    # Update the children count based on the movements
    for move in movement_string:
        # Increment the count for the current position before moving
        children_count[current_position] += 1
        # Move based on the character
        if move == 'R':
            current_position = min(N - 1, current_position + 1)  # Move right, ensure bounds
        elif move == 'L':
            current_position = max(0, current_position - 1)  # Move left, ensure bounds
    # Increment the count for the final position
    children_count[current_position] += 1
    return children_count