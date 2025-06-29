'''
Main application file for the Monster Battle game.
'''
from utils import validate_input, calculate_total_damage, check_health
def main():
    health_input = input("Enter Monster's Health (H, positive integer): ")
    # Validate health input
    if not validate_input(health_input):
        print("Please enter a valid positive integer for health.")
        return
    H = int(health_input)
    moves_input = input("Enter Special Moves (comma-separated positive integers, e.g., 10,20,30). Enter '0' if no moves: ")
    # Validate moves input
    if not validate_input(moves_input, is_moves=True):
        print("Please enter valid positive integer values for moves.")
        return
    # Handle edge case where user inputs '0' for no moves
    if moves_input.strip() == '0':
        moves = []
    else:
        moves = list(map(int, moves_input.split(',')))
    # Filter out any '0' moves
    moves = [move for move in moves if move > 0]
    # Handle edge case where N is 0 or contains invalid moves
    if len(moves) == 0:
        print("No")
        return
    total_damage = calculate_total_damage(moves)
    if total_damage < H:
        print("No")
        return
    moves.sort(reverse=True)
    result = check_health(H, moves)
    print(result)
if __name__ == "__main__":
    main()