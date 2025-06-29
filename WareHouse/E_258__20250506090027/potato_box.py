'''
Module for managing potato packing logic.
'''
class PotatoBox:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold
        self.boxes = []
    def pack_potatoes(self):
        current_weight = 0
        potato_count = 0
        cycle_length = len(self.weights)
        total_weight_in_cycle = sum(self.weights)
        # If total weight in one cycle is less than the threshold, no boxes can be packed
        if total_weight_in_cycle < self.threshold:
            return  # No boxes can be packed if the total weight in one cycle is less than the threshold
        while True:
            for i in range(cycle_length):
                weight = self.weights[i]
                current_weight += weight
                potato_count += 1
                # Check if the current box can be sealed
                if current_weight >= self.threshold:
                    self.boxes.append(potato_count)  # Seal the box
                    current_weight = 0  # Reset for the next box
                    potato_count = 0  # Reset potato count for the next box
                    # Break if we have reached the maximum number of boxes
                    if len(self.boxes) >= 10**12:
                        return
            # If we complete a full cycle and still can't pack more boxes, break the loop
            if potato_count == cycle_length and current_weight < self.threshold:
                break
    def get_box_count(self, k):
        if k <= len(self.boxes):
            return self.boxes[k - 1]
        else:
            return -1  # Indicate that the box does not exist