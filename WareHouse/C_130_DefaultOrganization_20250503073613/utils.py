'''
Utility functions for the Rectangle Area Calculator.
This module contains functions to validate input and calculate areas of sections
formed by cutting a rectangle through a specified point.
'''
def calculate_areas(W, H, x, y):
    '''
    Calculate the areas of the four sections formed by cutting the rectangle
    through the point (x, y) and return the maximum area of the smaller part
    and whether there are multiple ways to achieve that area.
    Parameters:
    W (int): Width of the rectangle.
    H (int): Height of the rectangle.
    x (int): X coordinate of the point.
    y (int): Y coordinate of the point.
    Returns:
    tuple: Maximum area of the smaller part and a boolean indicating if there are multiple ways to achieve that area.
    '''
    Area1 = x * y
    Area2 = (W - x) * y
    Area3 = (W - x) * (H - y)
    Area4 = x * (H - y)
    areas = [Area1, Area2, Area3, Area4]
    max_part_area = min(areas)
    multiple_ways = areas.count(max_part_area) > 1
    return max_part_area, multiple_ways