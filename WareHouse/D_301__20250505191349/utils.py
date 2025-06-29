'''
Utility functions for generating combinations and converting binary to decimal.
'''
def evaluate_combinations(s, n):
    '''
    Evaluate combinations of the string S by replacing '?' with '0' and '1'.
    Returns the maximum decimal value found that is less than or equal to N.
    '''
    # Validate input string
    if not s or any(char not in '01?' for char in s):
        raise ValueError("String S must not be empty and must only contain '0', '1', or '?' characters.")
    max_value = -1
    length = len(s)
    num_questions = s.count('?')
    # If there are no '?', directly convert and check
    if num_questions == 0:
        decimal_value = int(s, 2)
        return decimal_value if decimal_value <= n else -1
    # Iterate through all combinations using bit manipulation
    for i in range(1 << num_questions):  # 2^num_questions combinations
        current_string = list(s)
        question_index = 0
        for j in range(length):
            if current_string[j] == '?':
                # Replace '?' with '0' or '1' based on the current combination
                current_string[j] = '1' if (i & (1 << question_index)) > 0 else '0'
                question_index += 1
        # Check for leading zeros
        if current_string[0] == '0' and len(current_string) > 1 and ''.join(current_string) != '0':
            continue  # Skip this combination as it has leading zeros
        decimal_value = int(''.join(current_string), 2)
        if decimal_value <= n:
            max_value = max(max_value, decimal_value)
    return max_value