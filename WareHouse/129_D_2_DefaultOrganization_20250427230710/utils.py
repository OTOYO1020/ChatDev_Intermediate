'''
Utility functions for input validation.
'''
def validate_input(h, w, grid_input):
    try:
        h = int(h)
        w = int(w)
        if h <= 0 or w <= 0:
            return False
        if len(grid_input) != h:
            return False
        for row in grid_input:
            if len(row) != w or any(c not in '#.' for c in row):
                return False
        # Check for at least one empty square
        if all(row == '#' * w for row in grid_input):
            return False
        return True
    except ValueError:
        return False