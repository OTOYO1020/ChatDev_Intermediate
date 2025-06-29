'''
Utility functions for calculating maximum profit.
'''
def max_profit(num_towns, graph, prices):
    '''
    Calculate the maximum profit that can be achieved by buying gold
    in each town and selling it in reachable towns.
    '''
    max_profit_value = 0  # Start with 0 instead of negative infinity
    for town in range(num_towns):
        max_selling_price = graph.dfs(town, prices)  # Updated call to dfs
        profit = max_selling_price - prices[town]  # Calculate profit directly
        max_profit_value = max(max_profit_value, profit)
    return max_profit_value  # Return the maximum profit found