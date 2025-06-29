'''
Module for sorting a permutation array and counting swaps.
'''
class PermutationSorter:
    def __init__(self, array):
        self.array = array
    def validate_permutation(self):
        n = len(self.array)
        if len(set(self.array)) != n or sorted(self.array) != list(range(1, n + 1)):
            raise ValueError("Input array is not a valid permutation of numbers from 1 to N. Please ensure it contains unique integers from 1 to {}.".format(n))
    def sort(self):
        swap_count = 0
        n = len(self.array)
        self.validate_permutation()  # Validate the input permutation at the start
        # Check if the array is already sorted
        if self.array == list(range(1, n + 1)):
            return swap_count  # No swaps needed if already sorted
        # Continue sorting until the array is sorted
        i = 0
        while i < n:
            # Continue swapping until the current index has the correct value
            while self.array[i] != i + 1:
                j = self.array[i] - 1
                # Swap the elements at indices i and j
                self.array[i], self.array[j] = self.array[j], self.array[i]
                swap_count += 1
            i += 1  # Move to the next index only if the current index is correct
        return swap_count