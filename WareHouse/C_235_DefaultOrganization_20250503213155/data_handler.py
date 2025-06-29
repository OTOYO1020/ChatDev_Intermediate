'''
Data handler for managing the sequence of integers and occurrences.
'''
class DataHandler:
    def __init__(self, sequence):
        self.sequence = sequence
        self.occurrences = {}
        self.populate_occurrences()
    def populate_occurrences(self):
        for index, number in enumerate(self.sequence):
            if number not in self.occurrences:
                self.occurrences[number] = []
            self.occurrences[number].append(index)
    def get_kth_occurrence(self, x, k):
        if x in self.occurrences:
            indices = self.occurrences[x]
            if len(indices) < k:
                return -1
            return indices[k - 1]  # Adjust for 0-based indexing
        return -1