'''
Calculates the maximum profit from gold trading.
'''
from typing import List, Tuple
from graph import Graph
def max_profit(N: int, M: int, A: List[int], roads: List[Tuple[int, int]]) -> int:
    graph = Graph(N)
    for u, v in roads:
        if 1 <= u <= N and 1 <= v <= N:  # Validate town indices
            graph.add_edge(u, v)  # Keep 1-based indexing
        else:
            raise ValueError(f"Town indices must be between 1 and {N}. Invalid road: ({u}, {v})")
    max_profit_value = 0
    # Iterate through each town to calculate potential profits
    for town in range(1, N + 1):  # Change to 1-based indexing
        visited = set()
        reachable_prices = []  # To store prices of reachable towns
        # Use the DFS method to explore reachable towns
        graph.dfs(town, visited)
        # Collect prices of reachable towns
        for v in visited:
            reachable_prices.append(A[v - 1])  # Adjust for 0-based indexing when accessing prices
        # Check if there are reachable prices
        if not reachable_prices:
            continue  # Skip to the next town if no reachable towns
        # Initialize min_price with the price of the current town
        min_price = A[town - 1]
        # Calculate profit based on the min price and all reachable prices
        for price in reachable_prices:
            if price < min_price:
                min_price = price  # Update min price
            else:
                max_profit_value = max(max_profit_value, price - min_price)  # Calculate profit
    return max_profit_value