'''
Contains the function to count valid triangle combinations from stick lengths.
'''
def count_valid_triangles(lengths):
    count = 0
    n = len(lengths)
    # Iterate through all combinations of three distinct indices (0-based)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Check if lengths are all different
                if lengths[i] != lengths[j] and lengths[j] != lengths[k] and lengths[i] != lengths[k]:
                    # Check triangle inequality
                    if (lengths[i] + lengths[j] > lengths[k] and
                        lengths[i] + lengths[k] > lengths[j] and
                        lengths[j] + lengths[k] > lengths[i]):
                        count += 1
    return count