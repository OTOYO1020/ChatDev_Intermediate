'''
Logic file containing the function to process sequences.
'''
def f(x, a_i, t_i):
    '''
    Computes the result based on the value of t_i.
    Parameters:
    x (int): The current value to be processed.
    a_i (int): The integer from sequence A.
    t_i (int): The operation type (1, 2, or 3).
    Returns:
    int: The computed result based on the operation type.
    '''
    if t_i == 1:
        return x + a_i
    elif t_i == 2:
        return max(x, a_i)
    elif t_i == 3:
        return min(x, a_i)
    else:
        raise ValueError("Invalid value for t_i. Must be 1, 2, or 3.")