'''
Module for processing the color grid operations.
'''
def count_colors(H, W, M, operations):
    '''
    Counts the number of cells painted with each color after processing operations.
    '''
    # Initialize last color for rows and columns
    last_row_color = [0] * H
    last_col_color = [0] * W
    last_row_op = [-1] * H  # To track the last operation index for rows
    last_col_op = [-1] * W  # To track the last operation index for columns
    # Process operations
    for index, (T_i, A_i, X_i) in enumerate(operations):
        if T_i == 1:
            last_row_color[A_i - 1] = X_i
            last_row_op[A_i - 1] = index
        elif T_i == 2:
            last_col_color[A_i - 1] = X_i
            last_col_op[A_i - 1] = index
    # Count the colors in the grid
    color_count = {}
    for i in range(H):
        for j in range(W):
            # Determine the effective color for cell (i, j)
            if last_row_op[i] > last_col_op[j]:
                color = last_row_color[i]
            elif last_row_op[i] < last_col_op[j]:
                color = last_col_color[j]
            else:
                # If both operations are the same, we can choose either, but let's choose the row color
                color = last_row_color[i]
            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1
    return color_count