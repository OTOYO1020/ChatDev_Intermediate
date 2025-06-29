'''
Data processing module for counting boxes in the data.
'''
class DataProcessor:
    def __init__(self, data):
        self.data = data
    def count_boxes(self):
        if not self.data or not self.data[0]:  # Check if data is empty or has no columns
            return []
        counts = [0] * len(self.data[0])  # Assuming all rows have the same number of columns
        for row in self.data:
            for j, cell in enumerate(row):
                if cell not in ['#', '.']:  # Check for invalid characters
                    raise ValueError(f"Invalid character '{cell}' found in the grid.")
                if cell == '#':
                    counts[j] += 1
        return counts