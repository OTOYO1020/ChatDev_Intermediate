'''
Main application file for the teleportation simulation.
'''
from teleportation import find_final_town
def main():
    # Get user input for number of towns, teleport destinations, and number of teleportations
    N = int(input("Enter number of towns (N): "))
    A = list(map(int, input("Enter teleport destinations (A) as comma-separated values: ").split(',')))
    K = int(input("Enter number of teleportations (K): "))
    # Calculate the final town after K teleportations
    final_town = find_final_town(N, A, K)
    # Display the result
    print(f"Final Town: {final_town}")
if __name__ == "__main__":
    main()