'''
Main application file to run the Enemy Battle simulation.
'''
from battle import EnemyBattle
def main():
    # Read the number of enemies
    N = int(input("Enter the number of enemies: "))
    if N == 0:
        print("There are no enemies to battle.")
        return
    # Read the health values of the enemies
    health_values = []
    while len(health_values) != N:
        try:
            health_input = input("Enter the health values (comma-separated integers, e.g., 10,20,30) or type 'exit' to quit: ")
            if health_input.lower() == 'exit':
                print("Exiting the program.")
                return
            health_values = list(map(int, health_input.split(',')))
            if len(health_values) != N:
                print(f"Error: Expected {N} health values, but got {len(health_values)}.")
        except ValueError:
            print("Invalid input format. Please enter integers separated by commas (e.g., 10,20,30).")
    # Validate health values to ensure they are non-negative
    if any(h < 0 for h in health_values):
        print("Health values must be non-negative integers.")
        return
    # Initialize the battle with the health values
    battle = EnemyBattle(health_values)
    # Simulate the battle until all enemies are defeated
    while not battle.is_battle_over():
        battle.take_turn()
    # Print the total number of turns taken
    print(f"Total turns taken to defeat all enemies: {battle.get_turns()}")
if __name__ == "__main__":
    main()