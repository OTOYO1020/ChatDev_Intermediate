'''
Module containing the function to calculate minimum operations to make '1's contiguous.
'''
def min_operations_to_contiguous_ones(S: str) -> int:
    # Validate input string
    if not all(char in '01' for char in S):
        raise ValueError("Input string must only contain '0's and '1's.")
    # Parse the input string and determine its length
    N = len(S)
    # Identify the positions of all '1's in the string S
    positions = [i for i, char in enumerate(S) if char == '1']
    # Handle edge cases
    if len(positions) <= 1:
        return 0  # No operations needed if there's 0 or 1 '1'
    total_swaps = 0
    zero_count = 0  # To count the number of '0's crossed
    # Iterate through the string to count '0's and calculate swaps
    for i in range(N):
        if S[i] == '0':
            zero_count += 1
        elif S[i] == '1':
            # Calculate the target position for this '1'
            target_index = positions.index(i)  # Get the index of '1' in positions
            target = positions[0] + target_index  # Calculate the target position
            total_swaps += (i - target)  # Count how many '0's are crossed over
    return total_swaps