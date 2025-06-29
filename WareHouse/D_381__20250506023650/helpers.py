'''
Helper functions for finding the maximum length of a 1122 sequence.
'''
def find_max_length_1122_sequence(sequence):
    '''
    Finds the maximum length of a valid 1122 sequence in the given array.
    '''
    max_length = 0
    n = len(sequence)
    for start in range(n):
        count = {}
        for end in range(start, n):
            num = sequence[end]
            count[num] = count.get(num, 0) + 1
            # Check if the current subarray is valid
            if (end - start + 1) % 2 == 0:  # Length must be even
                unique_count = sum(1 for v in count.values() if v == 2)
                total_count = sum(count.values())
                # Ensure every integer appears exactly twice
                if unique_count == (end - start + 1) // 2 and total_count == (end - start + 1):
                    # Ensure no integer appears more than twice
                    if all(v <= 2 for v in count.values()):
                        # Ensure all integers that appear twice are the same
                        pairs = [k for k, v in count.items() if v == 2]
                        if len(pairs) == unique_count and len(pairs) == 1:  # Check if there's only one unique integer appearing twice
                            max_length = max(max_length, end - start + 1)
    return max_length