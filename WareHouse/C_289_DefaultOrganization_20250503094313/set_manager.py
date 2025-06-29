'''
Manages the sets of integers and calculates valid combinations.
'''
class SetManager:
    def __init__(self, m):
        self.sets = [set() for _ in range(m + 1)]  # Initialize with size M + 1 for 1-based indexing
    def add_set(self, index, numbers):
        unique_set = set(numbers)  # Convert to set to handle duplicates automatically
        if len(unique_set) < len(numbers):
            print(f"Warning: Duplicates found in the input for set {index}. Only unique values will be stored.")
        self.sets[index] = unique_set  # Store the unique set at the correct index
    def get_valid_count(self, n):
        return self.calculate_valid_combinations(n)
    def calculate_valid_combinations(self, n):
        valid_count = 0
        total_sets = len(self.sets) - 1  # Adjust for 1-based indexing
        # Iterate through all possible combinations of sets using bit manipulation
        for i in range(1, 1 << total_sets):
            chosen_set = set()
            for j in range(total_sets):
                if i & (1 << j):  # Check if the j-th set is included in the combination
                    chosen_set.update(self.sets[j + 1])  # Access using 1-based index
            # Check if the chosen set contains all integers from 1 to N
            if all(num in chosen_set for num in range(1, n + 1)):
                valid_count += 1
        return valid_count