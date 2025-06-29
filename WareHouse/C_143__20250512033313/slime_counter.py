'''
Module for counting distinct slimes after fusion.
'''
def count_fused_slimes(S: str) -> int:
    if not S:
        return 0  # Return 0 for empty string
    if len(S) == 1:
        return 1  # Return 1 for a single character string, as it represents one distinct slime
    fused_count = 1  # Start with 1 for the first distinct slime
    previous_char = S[0]  # Store the first character
    for i in range(1, len(S)):
        if S[i] != previous_char:
            fused_count += 1  # Increment for each distinct slime found
            previous_char = S[i]  # Update previous_char
    return fused_count  # Return the final count of distinct slimes