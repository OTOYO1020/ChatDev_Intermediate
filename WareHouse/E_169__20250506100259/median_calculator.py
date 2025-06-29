'''
Module for calculating the number of distinct median values.
'''
def count_distinct_median(N, A, B):
    # Sort the lower and upper bounds
    sorted_A = sorted(A)
    sorted_B = sorted(B)
    possible_medians = set()  # Use a set to store distinct median values
    if N % 2 == 1:  # Odd case
        median_index = N // 2
        # The median can take values from the maximum of A[median_index] to the minimum of B[median_index]
        min_median = sorted_A[median_index]
        max_median = sorted_B[median_index]
        for median in range(min_median, max_median + 1):
            possible_medians.add(median)
    else:  # Even case
        median_index1 = N // 2 - 1
        median_index2 = N // 2
        # Calculate the range for the two middle elements
        min_median = max(sorted_A[median_index1], sorted_A[median_index2])
        max_median = min(sorted_B[median_index1], sorted_B[median_index2])
        if min_median <= max_median:
            # Instead of using a range, we need to consider all values between the two bounds
            for median in range(min_median, max_median + 1):
                possible_medians.add(median)
    return len(possible_medians)  # Return the count of distinct median values