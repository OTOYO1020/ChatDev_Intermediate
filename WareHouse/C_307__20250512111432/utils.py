'''
Utility functions for checking sheet configurations.
'''
from sheet import Sheet
def can_create_sheet(H_A, W_A, A, H_B, W_B, B, H_X, W_X, X):
    # Create sheets A, B, and X
    sheet_a = Sheet(H_A, W_A, A)
    sheet_b = Sheet(H_B, W_B, B)
    sheet_x = Sheet(H_X, W_X, X)
    # Create a combined sheet C with dimensions that can fit both A and B
    max_height = max(H_A, H_B)  # Maximum height needed
    max_width = W_A + W_B  # Total width needed to place both sheets side by side
    sheet_c = Sheet(max_height, max_width, ';'.join(['0' * max_width for _ in range(max_height)]))  # Correct initialization
    # Check all possible placements of A and B
    for row_a in range(sheet_c.height):
        for col_a in range(sheet_c.width):
            if sheet_a.can_fit(row_a, col_a, sheet_c.grid):
                # Create a temporary grid to check placements
                temp_sheet_c = Sheet(sheet_c.height, sheet_c.width, ';'.join(['0' * max_width for _ in range(max_height)]))
                temp_sheet_c.paste(sheet_a, row_a, col_a)
                for row_b in range(sheet_c.height):
                    for col_b in range(sheet_c.width):
                        if sheet_b.can_fit(row_b, col_b, temp_sheet_c.grid):
                            # Create a new temporary grid for B placement
                            combined_sheet = Sheet(sheet_c.height, sheet_c.width, ';'.join(['0' * max_width for _ in range(max_height)]))
                            combined_sheet.paste(temp_sheet_c, 0, 0)  # Paste A first
                            combined_sheet.paste(sheet_b, row_b, col_b)  # Then paste B
                            # Check if combined_sheet matches sheet_x
                            if combined_sheet.matches(sheet_x):
                                return True
    return False