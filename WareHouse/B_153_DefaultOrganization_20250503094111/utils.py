'''
Utility functions for the Monster Battle game.
'''
def validate_input(value, is_moves=False):
    '''
    Validates the input value. If is_moves is True, checks for a list of positive integers.
    '''
    if is_moves:
        if not value.strip():  # Check for empty input
            return False
        moves = value.split(',')
        return all(move.strip().isdigit() for move in moves)  # Allow '0' but handle it later
    return value.isdigit() and int(value) > 0
def calculate_total_damage(moves):
    '''
    Calculates the total damage from the list of moves.
    '''
    return sum(moves)
def check_health(H, moves):
    '''
    Checks if the monster can be defeated based on the moves applied.
    '''
    current_health = H
    for move in moves:
        current_health -= move
        if current_health <= 0:
            return "Yes"
    return "No"