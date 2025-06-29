'''
Module for string comparison logic to calculate minimum character changes.
'''
class StringComparison:
    @staticmethod
    def calculate_min_changes(S, T):
        min_changes = float('inf')
        len_S = len(S)
        len_T = len(T)
        for i in range(len_S - len_T + 1):
            sub_S = S[i:i + len_T]
            changes = sum(1 for a, b in zip(sub_S, T) if a != b)
            min_changes = min(min_changes, changes)
        return min_changes if min_changes != float('inf') else -1  # Return -1 if no valid substring found