'''
Main application file for the consecutive 'X' calculator.
'''
def calculate_max_consecutive_X(S, K):
    # Check for edge cases
    if not S:  # If the string is empty
        return 0
    if K < 0:  # If K is negative
        raise ValueError("K must be a non-negative integer.")
    # Initialize the maximum count of consecutive 'X's
    max_consecutive_X = 0
    left = 0  # Left pointer for the sliding window
    dot_count = 0  # Count of '.' characters in the current window
    # Iterate through the string using the right pointer
    for right in range(len(S)):
        # If the current character is a '.', increment the dot count
        if S[right] == '.':
            dot_count += 1
        # If the dot count exceeds K, move the left pointer to reduce the window size
        while dot_count > K:
            if S[left] == '.':
                dot_count -= 1  # Decrease dot count if we are moving past a '.'
            left += 1  # Move the left pointer to the right
        # Calculate the length of the current window and update the maximum consecutive 'X's
        max_consecutive_X = max(max_consecutive_X, right - left + 1)
    return max_consecutive_X
if __name__ == "__main__":
    S = input("Enter string S: ")
    while True:
        try:
            K = int(input("Enter integer K (non-negative): "))
            if K < 0:
                print("K must be a non-negative integer. Please try again.")
                continue
            break  # Exit the loop if input is valid
        except ValueError:
            print("Please enter a valid integer for K.")
    result = calculate_max_consecutive_X(S, K)
    print(f"Max Consecutive X's: {result}")