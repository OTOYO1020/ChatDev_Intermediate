'''
Utility functions for the word fitting application.
'''
def can_fit_in_window(widths, window_width, max_lines):
    """
    Check if the words can fit within the specified window width
    while adhering to the maximum number of lines allowed.
    Parameters:
    - widths: List of integers representing the widths of the words.
    - window_width: The maximum width of the window.
    - max_lines: The maximum number of lines allowed.
    Returns:
    - True if the words fit within the constraints, False otherwise.
    """
    current_line_width = 0
    line_count = 1  # Start with one line
    for i in range(len(widths)):
        # Check if adding the current word exceeds the window width
        if current_line_width + (widths[i] + (1 if current_line_width > 0 else 0)) > window_width:
            line_count += 1
            current_line_width = widths[i]  # Start new line with the current word
            if line_count > max_lines:
                return False
        else:
            current_line_width += (widths[i] + (1 if current_line_width > 0 else 0))
    return True
def binary_search_min_width(widths, max_lines):
    """
    Perform binary search to find the minimum width required to fit all words
    within the specified maximum number of lines.
    Parameters:
    - widths: List of integers representing the widths of the words.
    - max_lines: Maximum number of lines allowed.
    Returns:
    - The minimum width required to fit the words.
    """
    left = max(widths)
    right = sum(widths) + (len(widths) - 1)
    while left < right:
        mid = (left + right) // 2
        if can_fit_in_window(widths, mid, max_lines):  # Ensure this line is correct
            right = mid
        else:
            left = mid + 1
    return left