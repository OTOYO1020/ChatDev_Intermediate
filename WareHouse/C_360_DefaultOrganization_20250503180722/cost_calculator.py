'''
Contains the logic for calculating the total minimum cost of moving items.
'''
import heapq
from collections import defaultdict, deque
class CostCalculator:
    def calculate(self, boxes, weights):
        '''
        Calculate the total minimum cost of moving items to ensure each box contains exactly one item.
        Parameters:
        boxes (list): List of box numbers for each item.
        weights (list): List of weights for each item.
        Returns:
        int: Total minimum cost incurred during the moving process.
        '''
        box_items = defaultdict(list)
        for i in range(len(boxes)):
            box_items[boxes[i]].append(weights[i])
        total_cost = 0
        excess_items = []
        empty_boxes = deque()  # Use deque for efficient popping from the front
        for box in range(1, max(boxes) + 1):
            items = box_items[box]
            if len(items) > 1:
                excess_items.extend(sorted(items))
            elif len(items) == 0:
                empty_boxes.append(box)  # Append to deque
        heapq.heapify(excess_items)
        while excess_items and empty_boxes:
            # Move as many items as possible to empty boxes
            while excess_items and empty_boxes:
                lightest_item = heapq.heappop(excess_items)
                target_box = empty_boxes.popleft()  # Efficiently pop from the front
                total_cost += lightest_item  # Cost is equal to weight for moving
        # Handle remaining excess items
        if excess_items:
            total_cost += sum(excess_items)  # Add the weight of unmovable items to the total cost
            print(f"Warning: {len(excess_items)} items could not be moved due to insufficient empty boxes. Total weight of unmovable items: {sum(excess_items)}.")
        return total_cost