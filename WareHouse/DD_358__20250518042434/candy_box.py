'''
Module containing the function to determine if candy boxes can be purchased.
'''
from typing import List, Tuple
def can_buy_boxes(N: int, M: int, prices: List[int], candies: List[int]) -> Tuple[bool, int]:
    # Combine prices and candies into a list of tuples and sort by price
    sorted_boxes = sorted(zip(prices, candies), key=lambda x: x[0])  # Sort by price
    total_cost = 0
    # Sort minimum candy requirements in ascending order
    sorted_candies = sorted(candies)
    for requirement in sorted_candies:
        found = False
        for i in range(len(sorted_boxes)):
            price, candy = sorted_boxes[i]
            if candy >= requirement:  # Check if box can satisfy requirement
                total_cost += price  # Add price to total cost
                sorted_boxes.pop(i)  # Remove the box from consideration
                found = True
                break
        if not found:  # If no suitable box is found
            return (False, 0)
    return (True, total_cost)  # All requirements satisfied