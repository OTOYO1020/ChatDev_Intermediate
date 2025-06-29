'''
Module for counting integers that do not contain the digit '7' in decimal and octal representations.
'''
def calculate_count(N):
    count = 0
    for i in range(1, N + 1):
        # Check if '7' is in the decimal representation of i
        if '7' in str(i):
            continue
        # Check if '7' is in the octal representation of i (excluding the '0o' prefix)
        if '7' in oct(i)[2:]:
            continue
        # Increment count for valid integers
        count += 1
    return count