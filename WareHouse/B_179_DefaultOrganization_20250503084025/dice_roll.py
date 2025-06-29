'''
Module to check for consecutive doublets in dice rolls.
'''
def check_doublets(dice_rolls):
    '''
    Check for consecutive doublets in a list of dice rolls.
    Parameters:
    dice_rolls (list of tuples): A list where each tuple contains two integers representing a dice roll.
    Returns:
    str: "YES" if there are at least one set of three consecutive doublets, otherwise "NO".
    '''
    doublet_count = 0
    N = len(dice_rolls)
    for i in range(N - 2):
        if (dice_rolls[i][0] == dice_rolls[i][1] and
            dice_rolls[i + 1][0] == dice_rolls[i + 1][1] and
            dice_rolls[i + 2][0] == dice_rolls[i + 2][1]):
            doublet_count += 1
    return "YES" if doublet_count >= 1 else "NO"