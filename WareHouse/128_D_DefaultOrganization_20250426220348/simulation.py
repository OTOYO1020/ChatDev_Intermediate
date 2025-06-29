'''
Simulation logic for the Jewel Collector game.
'''
def simulate_operations(V, N, K):
    max_sum = 0
    # Iterate over possible numbers of operations A (a) and B (b)
    for a in range(min(N, K) + 1):
        for b in range(min(N, K - a) + 1):
            if a + b <= K:
                # Collect jewels based on the values of a and b
                left_jewels = V[:a] if a > 0 else []  # Ensure a > 0 before slicing
                right_jewels = V[-b:] if b > 0 else []  # Ensure b > 0 before slicing
                hand = left_jewels + right_jewels
                remaining_operations = K - (a + b)
                # Calculate the current sum of jewels after optimization
                current_sum = optimize_jewels(hand, remaining_operations)
                max_sum = max(max_sum, current_sum)
    return max_sum
def optimize_jewels(hand, remaining_operations):
    if not hand:  # Check if hand is empty
        return 0
    hand.sort()
    # Ensure we do not discard more jewels than we have
    discard_count = min(remaining_operations, len(hand))
    hand = hand[discard_count:]  # Discard the lowest values
    return sum(hand)