'''
Utility functions for AtCoder contest series checker.
'''
def get_remaining_series(input_series, held_series):
    '''
    Calculate the remaining contest series that are held by AtCoder.
    Parameters:
    input_series (list): A list of contest series entered by the user.
    held_series (set): A set of contest series currently held by AtCoder.
    Returns:
    list: A list of remaining contest series after removing the input series.
    '''
    input_set = set(input_series)
    remaining_series = held_series - input_set
    return list(remaining_series)