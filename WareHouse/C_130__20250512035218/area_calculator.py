'''
Module for calculating the maximum area after cutting a rectangle.
'''
from typing import Tuple
def max_area_cut(W: int, H: int, x: int, y: int) -> Tuple[int, bool]:
    # Calculate the total area of the rectangle
    total_area = W * H
    # Determine the maximum area of the smaller part
    max_area = total_area // 2
    # Calculate the areas of the four parts created by the cut line
    area1 = x * y  # Area of the bottom-left part
    area2 = (W - x) * y  # Area of the bottom-right part
    area3 = x * (H - y)  # Area of the top-left part
    area4 = (W - x) * (H - y)  # Area of the top-right part
    # Check how many areas can equal max_area
    count = sum(1 for area in [area1, area2, area3, area4] if area == max_area)
    multiple_ways = count > 1  # Set to True if more than one area equals max_area
    return max_area, multiple_ways