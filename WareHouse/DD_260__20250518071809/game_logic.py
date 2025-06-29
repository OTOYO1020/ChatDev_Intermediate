'''
Game logic for determining which cards are eaten based on the rules.
'''
from typing import List
def find_eaten_cards(N: int, K: int, P: List[int]) -> List[int]:
    table = []  # Initialize the table to keep track of stacks of cards
    eaten_moves = [-1] * N  # Initialize with -1 for all cards
    for idx, card in enumerate(P):  # Use enumerate to get the index of the card
        X = card
        placed = False
        # Find the smallest stack on the table that has a top card >= X
        for stack in table:
            if stack[-1][0] >= X:  # Check the top card of the stack
                stack.append((card, idx))  # Stack the card on top with its index
                placed = True
                break
        if not placed:
            table.append([(card, idx)])  # Place the card face up on the table as a new stack
        # Check if we have at least K cards on the table
        if sum(len(stack) for stack in table) >= K:  # Count total cards on the table
            # Mark the last K cards as eaten
            cards_eaten = 0
            for stack in reversed(table):  # Start from the last stack
                while len(stack) > 0 and cards_eaten < K:  # Ensure we only pop if we still need to eat cards
                    card_info = stack.pop()  # Get the card info
                    eaten_moves[card_info[1]] = idx + 1  # Mark the original position as eaten
                    cards_eaten += 1
                if cards_eaten == K:  # Stop if we have eaten K cards
                    break
            # Remove empty stacks from the table
            table = [stack for stack in table if len(stack) > 0]
    return eaten_moves