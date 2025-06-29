'''
Module containing the function to count integers without the digit '7'.
'''
def count_integers_without_7(N: int) -> int:
    """
    Count integers from 1 to N that do not contain the digit '7'
    in their decimal or octal representation.
    Parameters:
    N (int): The upper limit of the range to check.
    Returns:
    int: The count of valid integers.
    """
    count = 0
    for i in range(1, N + 1):
        decimal_str = str(i)
        if '7' not in decimal_str:  # Check decimal representation first
            octal_str = oct(i)[2:]  # Get octal representation without '0o' prefix
            if '7' not in octal_str:  # Check octal representation
                count += 1
    return count