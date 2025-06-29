'''
Grid class for managing the grid and counting distinct numbers after blackout operations.
'''
class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [[0] * width for _ in range(height)]
    def populate_grid(self):
        '''
        Populates the grid with integers read from standard input.
        '''
        print("Enter the grid values row by row (space-separated):")
        for i in range(self.height):
            row = input(f"Row {i + 1}: ").strip().split()
            if len(row) != self.width:
                raise ValueError(f"Row {i + 1} must contain exactly {self.width} integers.")
            self.grid[i] = list(map(int, row))
    def count_distinct_numbers(self, h, w):
        '''
        Counts distinct numbers in the grid after applying blackout operations.
        '''
        distinct_counts = []
        for k in range(self.height - h + 1):
            for l in range(self.width - w + 1):
                visible_numbers = set()
                # Loop through only the relevant area outside the blackout region
                for i in range(self.height):
                    for j in range(self.width):
                        # Check if (i, j) is outside the blackout area
                        if not (k <= i < k + h and l <= j < l + w):
                            visible_numbers.add(self.grid[i][j])
                distinct_counts.append(len(visible_numbers))
        return distinct_counts