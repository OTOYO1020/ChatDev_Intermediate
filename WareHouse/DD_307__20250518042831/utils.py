'''
Utility functions for string processing.
'''
def remove_contiguous_substrings(S):
    '''
    Removes contiguous substrings based on parentheses from the input string.
    Args:
        S (str): The input string to process.
    Returns:
        str: The modified string after processing.
    '''
    stack = []
    result = []
    for char in S:
        if char == '(':
            stack.append(len(result))  # Store the current length of result
        elif char == ')':
            if stack:  # If there's a matching '('
                stack.pop()  # Pop the matching '('
            # If there's no matching '(', we do nothing (skip the ')')
        else:
            if not stack:  # Only add characters if there are no unmatched '('
                result.append(char)
    # If there are unmatched opening parentheses, we need to filter out the characters
    if stack:
        # Remove characters from the result that are within unmatched parentheses
        result = [result[i] for i in range(len(result)) if i < stack[0]]
    # Return the modified string after processing
    return ''.join(result)  # This will now only include characters outside of unmatched parentheses