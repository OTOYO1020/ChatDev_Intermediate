'''
Main application file for the height checking program.
'''
def check_heights(n, heights):
    """
    Checks if it is possible to achieve non-decreasing heights based on the given rules.
    Parameters:
    n (int): The number of squares.
    heights (list): A list of integers representing the heights of the squares.
    Returns:
    str: "YES" if non-decreasing order is possible, otherwise "NO" with an error message.
    """
    # Validate input: Check if n is positive
    if n <= 0:
        return "NO - The number of squares must be a positive integer."
    # Check if heights list is empty
    if n == 0 or not heights:
        return "NO - Heights list cannot be empty."
    # Check if the length of heights matches n
    if len(heights) != n:
        return f"NO - Expected {n} heights, but got {len(heights)}."
    # Check if all heights are non-negative integers
    if any(height < 0 for height in heights):
        return "NO - Heights must be non-negative integers."
    # Initialize previous_height to a value greater than any possible height
    previous_height = 10**9 + 1
    # Iterate through each height in the list
    for height in heights:
        # Check if the current height is greater than the previous height
        if height > previous_height:
            # If the current height minus one is still greater than or equal to previous_height
            if height - 1 >= previous_height:
                previous_height = height - 1  # Decrease the height
            else:
                previous_height = height  # Do nothing, keep the current height
        else:
            previous_height = height  # Set previous_height to the current height
    # If the loop completes without issues, return "YES"
    return "YES"
if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            heights = list(map(int, input().split()))
            result = check_heights(n, heights)
            print(result)
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter integers only.")