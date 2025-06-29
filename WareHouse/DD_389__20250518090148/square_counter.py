'''
Module to count the number of squares within a circle of radius R.
'''
def count_squares_within_circle(R):
    '''
    Counts the number of squares with corners within a circle of radius R.
    Parameters:
    R (int): The radius of the circle.
    Returns:
    int: The count of squares completely contained within the circle.
    '''
    count = 0
    # Determine the range for i and j based on R
    for i in range(-R + 1, R):  # Adjusted range to ensure squares are fully within the circle
        for j in range(-R + 1, R):  # Adjusted range to ensure squares are fully within the circle
            # Calculate the coordinates of the four corners of the square
            corners = [
                (i + 0.5, j + 0.5),
                (i + 0.5, j - 0.5),
                (i - 0.5, j + 0.5),
                (i - 0.5, j - 0.5)
            ]
            # Check if all corners are within the circle
            if all((x**2 + y**2 <= R**2) for x, y in corners):
                count += 1
    return count