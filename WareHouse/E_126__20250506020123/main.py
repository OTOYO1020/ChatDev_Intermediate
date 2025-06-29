'''
Main entry point of the card game application.
'''
from card import Card
from constraint import Constraint
import random
class CardGameApp:
    def __init__(self):
        self.N = 0
        self.M = 0
        self.cards = []
        self.constraints = []
        self.setup_ui()
    def setup_ui(self):
        print("Enter the number of Cards (N):")
        self.N = int(input())
        print("Enter the number of Constraints (M):")
        self.M = int(input())
        self.cards = [Card(i) for i in range(self.N)]
        self.constraints = []
        print("Enter constraints in the format 'X Y Z' for each constraint:")
        for _ in range(self.M):
            x, y, z = map(int, input().split())
            self.constraints.append(Constraint(x, y, z))
        self.deduce_values()
    def deduce_values(self):
        '''
        Deduce the values of the cards based on the constraints provided.
        The method iterates through the constraints and applies the parity conditions
        to infer unknown card values until no further deductions can be made.
        '''
        changed = True
        inconsistencies_found = False  # Track inconsistencies
        revealed_cards = set()  # Track revealed cards
        deduction_count = [0] * self.N  # Track how many times each card's value has been deduced
        while changed:
            changed = False
            for constraint in self.constraints:
                x_value = self.cards[constraint.x].value
                y_value = self.cards[constraint.y].value
                # Skip deduction if both values are unknown
                if x_value is None and y_value is None:
                    continue
                if x_value is not None and y_value is None:
                    # Deduce y_value based on x_value and z
                    new_value = (x_value + constraint.z) % 2
                    if self.cards[constraint.y].value is None:  # Only set if unknown
                        self.cards[constraint.y].value = new_value
                        changed = True
                        revealed_cards.add(constraint.y)
                        deduction_count[constraint.y] += 1
                    elif self.cards[constraint.y].value != new_value:
                        print(f"Inconsistent value for card {constraint.y}: expected {new_value}, found {self.cards[constraint.y].value}.")
                        inconsistencies_found = True
                elif y_value is not None and x_value is None:
                    # Deduce x_value based on y_value and z
                    new_value = (y_value + constraint.z) % 2
                    if self.cards[constraint.x].value is None:  # Only set if unknown
                        self.cards[constraint.x].value = new_value
                        changed = True
                        revealed_cards.add(constraint.x)
                        deduction_count[constraint.x] += 1
                    elif self.cards[constraint.x].value != new_value:
                        print(f"Inconsistent value for card {constraint.x}: expected {new_value}, found {self.cards[constraint.x].value}.")
                        inconsistencies_found = True
                elif x_value is not None and y_value is not None:
                    # Check if the parity condition holds
                    if (x_value + y_value) % 2 != constraint.z:
                        print(f"Inconsistent values for cards {constraint.x} and {constraint.y} with constraint {constraint.z}.")
                        inconsistencies_found = True  # Mark inconsistency
        # Count unknown cards and calculate cost
        total_cost = 0
        for card in self.cards:
            if card.value is None:
                total_cost += 1  # Increment cost for each unknown card revealed
                # Simulate revealing the card value
                revealed_value = self.simulate_reveal(card.index)  # Determine the value dynamically
                if revealed_value is not None:
                    card.value = revealed_value  # Only set if a valid value is revealed
                    revealed_cards.add(card.index)
        print(f"Total cost to reveal all cards: {total_cost}")
        if inconsistencies_found:
            print("Note: Some inconsistencies were found during deduction.")
    def simulate_reveal(self, index):
        '''
        Simulate revealing the value of an unknown card based on the current constraints.
        This method should ensure that the revealed value is consistent with the deductions made.
        '''
        # Check the constraints involving this card to determine a valid value
        possible_values = {0, 1}  # Start with both possible values
        for constraint in self.constraints:
            if constraint.x == index or constraint.y == index:
                other_index = constraint.y if constraint.x == index else constraint.x
                other_value = self.cards[other_index].value
                if other_value is not None:
                    # Deduce the value based on the known value and the constraint
                    expected_value = (other_value + constraint.z) % 2
                    possible_values.intersection_update({expected_value})
        # If we have deduced a possible value, return it; otherwise, indicate that the value cannot be determined
        if possible_values:
            return possible_values.pop()
        else:
            print(f"Warning: Unable to determine a value for card {index}.")
            return None  # Indicate that the value cannot be determined
if __name__ == "__main__":
    app = CardGameApp()