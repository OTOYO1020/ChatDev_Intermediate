'''
Utility functions for the player ranking system.
'''
def count_wins(results):
    '''
    Counts the number of wins for each player based on their match results.
    Parameters:
    results (list of str): List containing match results for each player.
    Returns:
    list of int: List containing the win counts for each player.
    '''
    return [result.count('o') for result in results]