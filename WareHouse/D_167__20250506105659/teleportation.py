'''
Module containing the teleportation logic.
'''
def find_final_town(N, K, A):
    '''
    Finds the final town after K teleportations using cycle detection.
    Parameters:
    N (int): Number of towns.
    K (int): Number of teleportations.
    A (list): List of teleportation destinations.
    Returns:
    int: The final town number after K teleportations.
    '''
    if K == 0:
        return 1  # If no teleportations, return the starting town
    slow = 1
    fast = 1
    # Detect cycle using Floyd's Tortoise and Hare algorithm
    for _ in range(N):  # Limit iterations to prevent infinite loops
        slow = A[slow - 1]  # Move slow by one step
        # Check if fast can move two steps
        if A[fast - 1] < 1 or A[fast - 1] > N:
            return slow  # Return the current town if no cycle is detected
        fast = A[A[fast - 1] - 1]  # Move fast by two steps
        # Check if slow and fast meet
        if slow == fast:
            break
    else:
        return slow  # If no cycle is detected after N iterations
    # Find the start of the cycle
    slow = 1
    while slow != fast:
        slow = A[slow - 1]
        fast = A[fast - 1]
    # Find the length of the cycle
    cycle_length = 1
    fast = A[slow - 1]
    while slow != fast:
        fast = A[fast - 1]
        cycle_length += 1
    # Calculate effective K
    current_town = 1
    steps_to_cycle_start = 0
    while current_town != slow:
        current_town = A[current_town - 1]
        steps_to_cycle_start += 1
    # Adjust K to be within the cycle length
    K = (K - steps_to_cycle_start) % cycle_length
    current_town = slow
    for _ in range(K):
        current_town = A[current_town - 1]
    return current_town