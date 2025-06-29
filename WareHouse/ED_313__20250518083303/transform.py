'''
Transformation functions for string manipulation.
'''
def f(S: str) -> str:
    """
    Transforms the input string S into a new string T based on the specified rules.
    Args:
    S (str): The input string consisting of digits from '1' to '9'.
    Returns:
    str: The transformed string T.
    Raises:
    ValueError: If the output exceeds the limit of 10^6 characters.
    """
    T = []
    for i in range(len(S) - 1):
        n = int(S[i + 1])  # Convert the next character to an integer
        T.append(S[i] * n)  # Append S[i] repeated n times to T
    result = ''.join(T)
    if len(result) > 10**6:  # Check if the final result exceeds the limit
        raise ValueError("Output exceeds the maximum allowed length of 10^6.")
    return result
def count_operations(S: str) -> int:
    """
    Counts the number of operations required to reduce the string S to length 1,
    or detects if the transformation results in an infinite cycle.
    Args:
    S (str): The input string consisting of digits from '1' to '9'.
    Returns:
    int: The number of operations modulo 998244353, or -1 if a cycle is detected or limit exceeded.
    """
    seen = set()
    counter = 0
    mod = 998244353
    while len(S) > 1:
        if S in seen:
            return -1  # Cycle detected
        seen.add(S)
        try:
            S = f(S)
        except ValueError:
            return -1  # Handle the case where output exceeds maximum length
        counter += 1
    return counter % mod