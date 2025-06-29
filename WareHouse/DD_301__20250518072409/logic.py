'''
Logic file containing the function to find the greatest value less than or equal to N.
'''
from itertools import product
def greatest_value_less_than_or_equal(N: int, S: str) -> int:
    # Validate input N
    if not (0 <= N <= 1000000):
        raise ValueError("N must be between 0 and 1,000,000.")
    # Validate input S
    if not S or any(c not in '01?' for c in S):
        raise ValueError("S must contain only '0', '1', or '?'.")
    # Initialize a set to store unique decimal values
    possible_values = set()
    # Generate combinations for '?' replacements
    question_marks = S.count('?')
    if question_marks == 0:
        # Directly convert S to decimal if no '?'
        decimal_value = int(S, 2)
        if decimal_value <= N:  # Check if the value is less than or equal to N
            possible_values.add(decimal_value)
    else:
        # Generate combinations for '?' replacements
        for bits in product('01', repeat=question_marks):
            temp_s = list(S)  # Convert to list to allow item assignment
            bit_index = 0
            for i in range(len(temp_s)):
                if temp_s[i] == '?':
                    temp_s[i] = bits[bit_index]
                    bit_index += 1
            # Convert the modified list back to string and then to decimal
            possible_values.add(int(''.join(temp_s), 2))
    # Filter values less than or equal to N
    valid_values = [value for value in possible_values if value <= N]
    # Return the maximum value or -1 if no valid values exist
    if valid_values:
        return max(valid_values)
    else:
        return -1