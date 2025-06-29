'''
Utility functions for calculating minimum swaps to transform a string into 'atcoder'.
'''
def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # Starting index for left subarray
    j = mid + 1 # Starting index for right subarray
    k = left    # Starting index to be sorted
    inv_count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)  # There are mid - i inversions
            j += 1
        k += 1
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
    return inv_count
def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)
    return inv_count
def count_inversions(S: str) -> int:
    arr = list(S)
    temp_arr = [0] * len(arr)
    return merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)
def min_operations_to_atcoder(S: str) -> int:
    """
    Calculate the minimum number of adjacent swaps needed to transform the string S into 'atcoder'.
    If S is not a permutation of 'atcoder', return -1.
    """
    target = 'atcoder'
    if not S:  # Check for empty input
        return -1
    if sorted(S) != sorted(target):
        return -1  # Not a valid permutation
    # Create a mapping of character positions in the target string
    target_positions = {char: [] for char in target}
    for index, char in enumerate(target):
        target_positions[char].append(index)
    # Create a list to track the current positions of characters in S
    current_positions = []
    char_count = {char: 0 for char in target}  # Track how many times we've used each character
    for char in S:
        pos_index = char_count[char]  # Get the current index for this character
        current_positions.append(target_positions[char][pos_index])  # Append the correct position
        char_count[char] += 1  # Increment the count for this character
    # Count inversions in current_positions to determine the number of swaps
    return count_inversions(current_positions)