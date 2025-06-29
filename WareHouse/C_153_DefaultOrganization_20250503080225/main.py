'''
Main application file for the Monster Attack game.
'''
from monster_attack import calculate_attacks
def main():
    # Read integers N and K from standard input
    n = int(input("Enter number of monsters (N): "))
    k = int(input("Enter number of special moves (K): "))
    # Read health of monsters as a list of integers
    h = list(map(int, input("Enter health of monsters (space-separated): ").split()))
    # Ensure the length of health matches N
    if len(h) != n:
        print("Error: The number of health values must match N.")
        return
    # Calculate total attacks needed
    total_attacks = calculate_attacks(n, k, h)
    # Print the result
    print(f"Total Attacks Required: {total_attacks}")
if __name__ == "__main__":
    main()