import math
class Subtask:
    def find_matching_indices(self, A, B):
        '''
        Find the number of matching indices without considering key change.
        Args:
            A (list): Sequence A
            B (list): Sequence B
        Returns:
            int: Number of matching indices
        '''
        if len(A) < len(B):
            return 0
        count = 0
        for i in range(len(A) - len(B) + 1):
            subsequence = A[i:i+len(B)]
            if subsequence == B:
                count += 1
        return count
    def find_matching_indices_with_key_change(self, A, B):
        '''
        Find the number of matching indices considering key change.
        Args:
            A (list): Sequence A
            B (list): Sequence B
        Returns:
            int: Number of matching indices
        '''
        if len(A) < len(B):
            return 0
        count = 0
        for i in range(len(A) - len(B) + 1):
            subsequence = A[i:i+len(B)]
            if self.is_matching_with_key_change(subsequence, B):
                count += 1
        return count
    def is_matching_with_key_change(self, subsequence, B):
        '''
        Check if a subsequence matches with key change.
        Args:
            subsequence (list): Subsequence of A
            B (list): Sequence B
        Returns:
            bool: True if the subsequence matches with key change, False otherwise
        '''
        if len(subsequence) != len(B):
            return False
        for i in range(len(subsequence)):
            if B[i] == 0:
                if subsequence[i] != 0:
                    return False
            elif B[i] != 0:
                key_change = subsequence[i] / B[i]
                if not math.isclose(subsequence[i], B[i] * key_change):
                    return False
        return True