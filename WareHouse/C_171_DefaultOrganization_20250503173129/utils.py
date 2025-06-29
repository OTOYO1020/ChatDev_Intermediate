'''
Utility functions for input validation and index-to-name conversion.
'''
def validate_input(n):
    return 1 <= n <= 1000000000000001
def index_to_name(index):
    name = []
    index += 1  # Adjust for one-based index
    while index > 0:
        index -= 1  # Adjust for zero-based index
        name.append(chr((index % 26) + ord('a')))
        index //= 26  # Move to the next "digit"
    return ''.join(reversed(name))