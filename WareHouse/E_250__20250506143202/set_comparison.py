'''
Contains logic for comparing sets derived from the sequences.
'''
class SetComparison:
    def compare_sets(self, prefix_sets_a, prefix_sets_b, queries):
        results = []
        for x_i, y_i in queries:
            # Handle cases where x_i or y_i is out of bounds
            if x_i < 1 or x_i > len(prefix_sets_a) or y_i < 1 or y_i > len(prefix_sets_b):
                results.append("No")  # This can be modified to provide more context if needed
                continue
            # Use the last valid set if x_i or y_i is valid
            set_a = prefix_sets_a[x_i - 1]  
            set_b = prefix_sets_b[y_i - 1]  
            # Compare the sets and append the result
            results.append("Yes" if set_a == set_b else "No")
        return results