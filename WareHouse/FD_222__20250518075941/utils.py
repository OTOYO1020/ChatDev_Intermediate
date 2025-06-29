'''
Utility functions for input handling and displaying results.
'''
from typing import List, Tuple
def get_input_data(input_data: str) -> Tuple[int, List[Tuple[int, int, int]], List[int]]:
    lines = input_data.strip().split('\n')
    if len(lines) < 2:
        raise ValueError("Insufficient input data. Please provide towns, roads, and sightseeing costs.")
    towns = int(lines[0])
    if towns <= 0:
        raise ValueError("The number of towns must be greater than zero.")
    roads = []
    # Check if there are lines for roads
    if len(lines) > 2:
        for road in lines[1:-1]:
            try:
                a, b, cost = map(int, road.split())
                if a < 1 or a > towns or b < 1 or b > towns:
                    raise ValueError("Town indices must be between 1 and the number of towns.")
                roads.append((a - 1, b - 1, cost))  # Adjusting indices to be zero-based
            except ValueError:
                raise ValueError("Each road must be specified as 'A B C' where A and B are town indices and C is the toll cost.")
    # If there are no roads, ensure roads list remains empty
    sightseeing_costs = list(map(int, lines[-1].split()))
    if len(sightseeing_costs) != towns:
        raise ValueError("The number of sightseeing costs must match the number of towns.")
    return towns, roads, sightseeing_costs
def display_results(text_widget, results: List[int]):
    text_widget.delete("1.0", END)
    text_widget.insert(END, "Maximum Travel Costs:\n")
    for i, cost in enumerate(results):
        if cost == -1:
            text_widget.insert(END, f"Town {i}: Isolated\n")
        else:
            text_widget.insert(END, f"Town {i}: {cost}\n")