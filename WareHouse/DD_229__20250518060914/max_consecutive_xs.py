'''
Module to calculate the maximum number of consecutive 'X's in a string after performing operations.
'''
def max_consecutive_Xs(S: str, K: int) -> int:
    # Check if there are no 'X's in the string
    if 'X' not in S:
        return K  # We can convert up to K '.' to 'X'
    max_count = 0  # Variable to track the maximum number of consecutive 'X's
    left = 0  # Left boundary of the sliding window
    dot_count = 0  # Count of '.' characters in the current window
    # Iterate through the string using the right boundary of the window
    for right in range(len(S)):
        if S[right] == '.':
            dot_count += 1  # Increment dot count if current character is '.'
        # If the count of '.' exceeds K, move the left boundary to reduce the count
        while dot_count > K:
            if S[left] == '.':
                dot_count -= 1  # Decrease dot count if we are moving past a '.'
            left += 1  # Move the left boundary to the right
        # Update max_count with the size of the current valid window
        max_count = max(max_count, right - left + 1)
    return max_count