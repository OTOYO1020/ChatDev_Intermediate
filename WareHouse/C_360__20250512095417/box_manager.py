'''
BoxManager class to handle box data and calculate minimum rearrangement cost.
'''
class BoxManager:
    def __init__(self, N, A, W):
        self.N = N
        self.A = A
        self.W = W
        self.boxes = {}
        self.total_cost = 0
        self._initialize_boxes()
    def _initialize_boxes(self):
        for i in range(self.N):
            box_number = self.A[i]
            weight = self.W[i]
            if box_number not in self.boxes:
                self.boxes[box_number] = []
            self.boxes[box_number].append(weight)
    def min_cost_to_rearrange_boxes(self):
        excess_boxes = []
        empty_boxes = [i for i in range(1, max(self.A) + 1) if i not in self.boxes]  # Identify empty boxes
        for box, weights in self.boxes.items():
            if len(weights) > 1:
                excess_boxes.append((box, weights))
        # Process excess boxes
        while excess_boxes:
            moved = False  # Flag to check if any item was moved in this iteration
            new_excess_boxes = []  # Track boxes that still have excess items
            for box, weights in excess_boxes:
                weights.sort()  # Sort weights to prioritize lighter items
                while len(weights) > 1 and empty_boxes:  # Ensure there are empty boxes available
                    item_weight = weights.pop()  # Remove the heaviest item
                    empty_box = empty_boxes.pop(0)  # Get an empty box
                    self.total_cost += item_weight  # Cost is the weight of the item moved
                    self.boxes[empty_box] = [item_weight]  # Place item in the empty box
                    moved = True  # Mark that we moved an item
                # Update new_excess_boxes if there are still excess items
                if len(weights) > 1:  # If there are still excess items, add to the new list
                    new_excess_boxes.append((box, weights))
            excess_boxes = new_excess_boxes  # Update excess_boxes for the next iteration
            if not moved:  # If no items were moved, break to avoid infinite loop
                break  # This break is now correctly placed within the while loop
        # Check if there are still excess items after all possible moves
        for box, weights in excess_boxes:
            while len(weights) > 1:
                item_weight = weights.pop()  # Remove the heaviest item
                self.total_cost += item_weight  # Cost is the weight of the item moved
                # If no empty boxes left, we cannot move anymore
                if not empty_boxes:
                    # Handle remaining excess items by consolidating them into existing boxes
                    lightest_item = min(weights)  # Find the lightest item
                    weights.remove(lightest_item)  # Remove it from the excess box
                    self.total_cost += lightest_item  # Add its weight to the cost
                    # Place it in a box that already has one item
                    for b in self.boxes:
                        if len(self.boxes[b]) == 1:
                            self.boxes[b].append(lightest_item)  # Add to this box
                            break
                    break  # Exit the loop as we can no longer move items
        return self.total_cost