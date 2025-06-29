'''
Main application file for the Enemy Defeat application.
'''
import sys
from enemy_defeat import calculate_time_to_defeat_enemies
def main():
    '''
    Main function to handle input and output for the Enemy Defeat application.
    '''
    try:
        N = int(input("Enter number of enemies: "))
        health_values = list(map(int, input("Enter health values (comma-separated): ").split(',')))
        if len(health_values) != N:
            raise ValueError("Number of health values must match the number of enemies.")
        time_taken = calculate_time_to_defeat_enemies(N, health_values)
        print(f"Time to defeat enemies: {time_taken}")
    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
if __name__ == "__main__":
    main()