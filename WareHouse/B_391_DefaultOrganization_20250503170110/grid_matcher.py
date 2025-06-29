'''
This module contains the GridMatcher class which is responsible for finding
the position of grid T within grid S.
'''
class GridMatcher:
    def __init__(self, grid_s, grid_t):
        self.grid_s = grid_s
        self.grid_t = grid_t
    def find_match(self):
        n = len(self.grid_s)
        m = len(self.grid_t)
        # Iterate over all possible top-left positions (a, b) in grid S
        for a in range(n - m + 1):  # Valid starting positions for rows
            for b in range(n - m + 1):  # Valid starting positions for columns
                match_found = True
                for i in range(m):
                    for j in range(m):
                        # Ensure correct indexing for grid S
                        if self.grid_s[a + i][b + j] != self.grid_t[i][j]:
                            match_found = False
                            break
                    if not match_found:
                        break
                if match_found:
                    return (a + 1, b + 1)  # Return 1-based index
        return None