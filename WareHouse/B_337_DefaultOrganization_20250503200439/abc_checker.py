'''
Module to check if a string is an Extended ABC string.
'''
def is_extended_abc_string(S):
    '''
    Determines if the input string S is an Extended ABC string.
    '''
    if not S:  # Check for empty string
        return "No"
    count_A = 0
    count_B = 0
    count_C = 0
    is_extended_abc = False
    last_A_index = -1
    first_C_index = -1
    for i, char in enumerate(S):
        if char == 'A':
            count_A += 1
            last_A_index = i
        elif char == 'B':
            count_B += 1
            if last_A_index == -1:  # B appears before any A
                return "No"  # Return immediately if invalid
        elif char == 'C':
            count_C += 1
            if first_C_index == -1:
                first_C_index = i
    if count_A > 0 and count_C > 0:
        if last_A_index < first_C_index:
            is_extended_abc = True
            # Check if all B's are strictly between the last A and the first C
            for i in range(last_A_index + 1, first_C_index):
                if S[i] != 'B':
                    is_extended_abc = False
                    break
            # Ensure no B's appear after the first C
            if 'B' in S[first_C_index:]:
                is_extended_abc = False
        else:
            is_extended_abc = False  # Invalidate if last A is not before first C
    else:
        is_extended_abc = False  # Ensure is_extended_abc is false if conditions are not met
    return "Yes" if is_extended_abc else "No"