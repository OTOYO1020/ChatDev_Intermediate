'''
Utility functions for string formation logic.
'''
def calculate_min_cost(target, bags):
    '''
    Calculate the minimum cost to form the target string using the strings from the bags.
    Parameters:
    target (str): The target string to be formed.
    bags (list of list of str): A list containing lists of strings (bags).
    Returns:
    int: The minimum cost to form the target string, or -1 if it cannot be formed.
    '''
    target_length = len(target)
    dp = [float('inf')] * (target_length + 1)
    dp[0] = 0  # Cost to form an empty string is 0
    # Iterate through each position in the target string
    for i in range(target_length):
        if dp[i] == float('inf'):
            continue  # Skip if this index is unreachable
        # Check each bag for possible strings
        for bag in bags:
            for string in bag:
                # If the target starts with the current string at position i
                if target.startswith(string, i):
                    # Increment cost by 1 for each string used
                    dp[i + len(string)] = min(dp[i + len(string)], dp[i] + 1)
    # Check if we can form the target string
    return dp[target_length] if dp[target_length] != float('inf') else -1