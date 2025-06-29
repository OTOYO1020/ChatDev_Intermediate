'''
Module for calculating the maximum score based on game rules.
'''
def max_score(N: int, K: int, R: int, S: int, P: int, T: str) -> int:
    score = 0
    last_used = [''] * K  # Initialize last used hands with empty strings
    current_index = 0  # Track the current index for last_used
    for i in range(N):
        machine_hand = T[i]
        optimal_hand = ''
        # Determine the optimal hand to play
        if machine_hand == 'R':
            optimal_hand = 'P'  # Paper beats Rock
        elif machine_hand == 'S':
            optimal_hand = 'R'  # Rock beats Scissors
        elif machine_hand == 'P':
            optimal_hand = 'S'  # Scissors beat Paper
        # Ensure the optimal hand is not the same as the hand used K rounds ago
        if i >= K and optimal_hand == last_used[(current_index - K) % K]:
            found_alternative = False
            available_hands = ['R', 'P', 'S']
            # First, try to find a winning hand that is not in last_used and not the hand used K rounds ago
            for hand in available_hands:
                if hand not in last_used and hand != last_used[(current_index - K) % K]:  # Ensure it's not the same as any last used hand or K rounds ago
                    # Ensure the alternative hand can win against the machine's hand
                    if (hand == 'R' and machine_hand == 'S') or \
                       (hand == 'P' and machine_hand == 'R') or \
                       (hand == 'S' and machine_hand == 'P'):
                        optimal_hand = hand
                        found_alternative = True
                        break
            # If no winning hand is found, select any available hand that is not in last_used and not the hand used K rounds ago
            if not found_alternative:
                for hand in available_hands:
                    if hand not in last_used and hand != last_used[(current_index - K) % K]:  # Ensure it's not the same as any last used hand or K rounds ago
                        optimal_hand = hand
                        break
        # Update score based on the optimal hand played
        if optimal_hand == 'R':
            score += R
        elif optimal_hand == 'S':
            score += S
        elif optimal_hand == 'P':
            score += P
        # Update last used hands
        last_used[current_index] = optimal_hand  # Update the current index
        current_index = (current_index + 1) % K  # Move to the next index
    return score