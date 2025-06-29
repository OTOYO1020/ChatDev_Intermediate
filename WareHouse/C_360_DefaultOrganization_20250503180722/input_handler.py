'''
Handles user input for box numbers and item weights.
'''
class InputHandler:
    def get_input(self, N, box_numbers, item_weights):
        boxes = list(map(int, box_numbers.split()))
        weights = list(map(int, item_weights.split()))
        if len(boxes) != N or len(weights) != N:
            raise ValueError("The number of boxes and weights must match N.")
        return boxes, weights