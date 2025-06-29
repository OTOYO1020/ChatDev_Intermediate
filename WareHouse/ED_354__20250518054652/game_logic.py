'''
Contains the game logic for determining the winner of the card game.
'''
from card import Card
from typing import List
class GameLogic:
    def __init__(self):
        self.cards = []
        self.current_player = 0  # 0 for Takahashi, 1 for Aoki
    def determine_winner(self, N: int, A: List[int], B: List[int]) -> str:
        # Initialize game state with cards
        self.cards = [Card(A[i], B[i]) for i in range(N)]
        while True:
            # Check for valid moves
            if not self.remove_pairs():
                break  # No valid moves, exit the loop
            # Switch players
            self.current_player = 1 - self.current_player
        # Determine winner based on the current player
        return "Takahashi" if self.current_player == 1 else "Aoki"
    def remove_pairs(self) -> bool:
        '''
        Logic to remove pairs of cards. This method allows for multiple rounds of pair removals
        in a single turn until no more pairs can be found.
        '''
        found_pair = False
        while True:
            to_remove = set()
            seen = {}
            # Count occurrences of front and back values
            for card in self.cards:
                front = card.front_value
                back = card.back_value
                seen[front] = seen.get(front, 0) + 1
                seen[back] = seen.get(back, 0) + 1
            # Identify values that have pairs
            for value, count in seen.items():
                if count >= 2:
                    to_remove.add(value)
            # Remove cards that have front or back values in to_remove
            if to_remove:
                found_pair = True
                self.cards = [card for card in self.cards if card.front_value not in to_remove and card.back_value not in to_remove]
            else:
                break  # Exit if no pairs found in this round
        return found_pair