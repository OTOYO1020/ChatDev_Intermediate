'''
Contains the logic for counting valid integers based on the input string and maximum value.
'''
def count_valid_integers(X: str, M: int) -> int:
    # Validate that all characters in X are digits
    if not all(char.isdigit() for char in X):
        return 0  # Return 0 if there are non-digit characters in X
    d = int(max(X))  # Extract the greatest digit and convert to integer
    if d > M:
        return 0  # Return 0 if the maximum digit exceeds M
    n = d + 1       # Minimum base
    count = 0       # Initialize counter
    while n <= M + 1:
        # Validate that all characters in X are valid digits for base n
        if all(int(char) < n for char in X):
            try:
                value = int(X, n)  # Convert string X to integer in base n
                if value <= M:
                    count += 1     # Increment count if valid
            except ValueError:
                break  # Break if conversion fails (invalid base)
        n += 1  # Increment base
    return count