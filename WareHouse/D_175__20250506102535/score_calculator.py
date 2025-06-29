'''
Contains the logic to calculate the maximum score based on the provided inputs.
'''
def calculate_score(n, k, c, p):
    # Validate input lengths
    if len(c) != n or len(p) != n:
        raise ValueError("Length of scores and permutation must match N.")
    # Validate uniqueness and range of values in permutation array
    if len(set(p)) != n:
        raise ValueError("Permutation values must be unique.")
    if any(value < 1 or value > n for value in p):
        raise ValueError("All permutation values must be between 1 and N (inclusive).")
    max_score = 0  # Initialize max_score to track the highest score found
    # Iterate through each starting square from 1 to N
    for i in range(1, n + 1):
        current_score = 0  # Initialize current_score for this starting position
        current_position = i  # Set the current position to the starting square
        visited = set()  # Create a set to track visited squares
        # If K is 0, add the score of the starting position directly
        if k == 0:
            current_score += c[current_position - 1]
            max_score = max(max_score, current_score)
            continue
        # Iterate exactly K times or until a cycle is detected
        for _ in range(k):  # Iterate exactly K times
            if current_position in visited:  # Check for cycles
                break  # Exit the loop if a cycle is detected
            visited.add(current_position)  # Mark the current position as visited
            # Get the next position from P
            next_position = p[current_position - 1]  # Adjusted for 0-based indexing
            # Ensure the next position is valid before accessing C
            if next_position < 1 or next_position > n:  # Check for out-of-bounds access
                raise IndexError("Attempted to access an index out of bounds in array C.")
            current_score += c[next_position - 1]  # Add the score from the current position
            current_position = next_position  # Move to the next position based on P
        max_score = max(max_score, current_score)  # Update max_score if current_score is higher
    return max_score  # Return the maximum score found