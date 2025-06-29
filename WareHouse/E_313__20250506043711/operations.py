'''
Contains the function to transform the input string according to specified rules.
'''
def f(S):
    if len(S) < 2:  # Handle case where S has less than 2 characters
        raise ValueError("Input string must have at least two characters.")
    T = []
    for i in range(len(S) - 1):
        if S[i + 1].isdigit():  # Check if the next character is a digit
            n = int(S[i + 1])  # Convert the next character to an integer
            # Only append if n is greater than 0
            if n > 0:  
                T.append(S[i] * n)  # Append n copies of S[i] to T
    if not T:  # Check if T is empty after processing
        return ""  # Return an empty string if T is empty to prevent infinite loop
    return ''.join(T)  # Join the list into a single string before returning