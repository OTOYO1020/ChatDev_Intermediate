'''
Utility functions for counting equal pairs in a list of integers.
'''
def count_equal_pairs(N, A):
    results = []
    frequency = {}
    # Build the initial frequency dictionary
    for num in A:
        frequency[num] = frequency.get(num, 0) + 1
    # Function to calculate total pairs from frequency dictionary
    def calculate_total_pairs(freq):
        return sum(count * (count - 1) // 2 for count in freq.values() if count > 1)
    # Calculate initial total pairs
    total_pairs = calculate_total_pairs(frequency)
    # Iterate over each k from 1 to N
    for k in range(1, N + 1):
        current_value = A[k - 1]
        # Decrease the frequency of the current value
        if current_value in frequency:
            frequency[current_value] -= 1
            if frequency[current_value] == 0:
                del frequency[current_value]  # Remove from dictionary if count is zero
        # Recalculate total pairs after excluding current_value
        total_pairs = calculate_total_pairs(frequency)
        # Store the result for the current k
        results.append(total_pairs)
        # Restore the frequency for the next iteration
        if current_value in frequency:
            frequency[current_value] += 1
        else:
            frequency[current_value] = 1  # Restore it to 1 if it was removed
    return results