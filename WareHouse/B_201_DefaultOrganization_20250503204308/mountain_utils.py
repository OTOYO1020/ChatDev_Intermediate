'''
Utility functions for mountain height calculations.
'''
def find_second_highest_mountain(mountains):
    """
    Finds the name of the second highest mountain from a list of mountains.
    Parameters:
    mountains (list): A list of tuples where each tuple contains (height, name).
    Returns:
    str: The name of the second highest mountain.
    Raises:
    ValueError: If there are not enough distinct mountains.
    """
    # Create a sorted list of distinct heights
    distinct_heights = sorted(set(mountain[0] for mountain in mountains), reverse=True)
    # Check if there are at least two distinct heights
    if len(distinct_heights) < 2:
        raise ValueError("There are not enough distinct mountains to determine the second highest.")
    # Get the second highest height
    second_highest = distinct_heights[1]
    # Find the mountain(s) with the second highest height
    second_highest_mountains = [mountain[1] for mountain in mountains if mountain[0] == second_highest]
    # Return the first mountain with the second highest height (if there are multiple)
    if second_highest_mountains:
        return second_highest_mountains[0]  # Return the first one found
    else:
        raise ValueError("No mountain found with the second highest height.")