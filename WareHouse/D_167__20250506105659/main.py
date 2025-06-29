'''
Main application file for the teleportation simulation.
'''
from teleportation import find_final_town
def main():
    '''
    Main function to run the teleportation simulation.
    '''
    try:
        n = int(input("Enter number of towns (N): "))
        k = int(input("Enter number of teleportations (K): "))
        a = list(map(int, input("Enter teleportation destinations (comma-separated, e.g., 2,3,1): ").strip().split(',')))
        if len(a) != n:
            raise ValueError("The number of destinations must match N.")
        if any(destination < 1 or destination > n for destination in a):
            raise ValueError("All teleportation destinations must be between 1 and N.")
        final_town = find_final_town(n, k, a)
        print(f"The final town after {k} teleportations is: {final_town}")
    except ValueError as ve:
        print(f"Input Error: {str(ve)}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
if __name__ == "__main__":
    main()