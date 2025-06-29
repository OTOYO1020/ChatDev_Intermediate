'''
Main entry point of the application that handles user interactions and calculations.
'''
from bulb import Bulb
from utils import generate_combinations, validate_bulbs
def main():
    # Read integers N and M from standard input
    try:
        N, M = map(int, input("Enter number of switches (N) and bulbs (M): ").split())
    except ValueError:
        print("Invalid input. Please enter two integers.")
        return
    # Initialize a list to store the connections of each bulb to the switches
    bulbs = []
    # For each bulb (from 1 to M)
    for i in range(M):
        try:
            k_i = int(input(f"Enter number of connected switches for Bulb {i + 1}: "))
            if k_i > 0:
                switches = list(map(int, input(f"Enter the {k_i} connected switch indices (comma-separated): ").split(',')))
                # Ensure all indices are valid
                if any(s < 1 or s > N for s in switches):
                    print(f"Some switch indices were invalid for Bulb {i + 1}. Please enter indices between 1 and {N}.")
                    continue  # Skip to the next iteration to re-prompt for valid input
            else:
                switches = []
            p_i = int(input(f"Enter the required parity (0 or 1) for Bulb {i + 1}: "))
            if p_i not in (0, 1):
                print("Parity must be 0 or 1. Please try again.")
                continue
            bulbs.append(Bulb(switches, p_i))
        except ValueError:
            print("Invalid input. Please enter integers only.")
            continue
    # Calculate valid combinations
    valid_count = calculate_valid_combinations(N, bulbs)
    # Print the total count of valid combinations
    print(f"Total valid combinations: {valid_count}")
def calculate_valid_combinations(n, bulbs):
    '''Calculate the number of valid combinations of switch states that satisfy all bulbs.'''
    combinations = generate_combinations(n)
    valid_count = sum(validate_bulbs(comb, bulbs) for comb in combinations)
    return valid_count
if __name__ == "__main__":
    main()