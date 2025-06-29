'''
Module to count distinct slimes based on their colors.
'''
def count_slimes(s):
    '''
    Count the number of distinct slimes after fusion based on the color string.
    Parameters:
    s (str): A string representing the colors of the slimes.
    Returns:
    int: The count of distinct slimes.
    '''
    slime_count = 0
    previous_color = ""
    for color in s:
        if color != previous_color:
            slime_count += 1
            previous_color = color
    return slime_count