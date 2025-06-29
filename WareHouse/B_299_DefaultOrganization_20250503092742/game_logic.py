'''
Contains the logic to determine the winner of the card game.
'''
def find_max_rank_player(players, ranks):
    '''
    Find the player with the maximum rank among the given players.
    Parameters:
    players (list): List of player indices.
    ranks (list): List of player ranks.
    Returns:
    int: The one-indexed ID of the player with the maximum rank, or None if no players are provided.
    '''
    if not players:  # Check if the players list is empty
        return None  # Or raise an exception as per your design choice
    max_rank = -1
    winner_id = -1
    for player_id in players:
        if ranks[player_id] > max_rank:
            max_rank = ranks[player_id]
            winner_id = player_id
    return winner_id + 1 if winner_id != -1 else None  # Ensure winner_id is one-indexed
def find_winner(N, colors, ranks, T):
    '''
    Determine the winner of the card game based on the specified color T.
    Parameters:
    N (int): Number of players.
    colors (list): List of colors of each player's card.
    ranks (list): List of ranks of each player's card.
    T (str): The color to check for determining the winner.
    Returns:
    int: The one-indexed ID of the winner, or None if no valid winner exists.
    '''
    players_with_color_T = [i for i in range(N) if colors[i] == T]
    if players_with_color_T:
        return find_max_rank_player(players_with_color_T, ranks)  # This is correct
    else:
        if N > 0:  # Ensure there are players before accessing player 1's color
            color_of_player_1 = colors[0]
            players_with_color_1 = [i for i in range(N) if colors[i] == color_of_player_1]
            return find_max_rank_player(players_with_color_1, ranks)  # This is correct
    return None  # No players to determine a winner