'''
Main application file for the bulb-switch combination calculator.
'''
from bulb import Bulb
def main():
    # Read integers N and M from standard input
    N = int(input("Enter the number of switches (N): "))
    M = int(input("Enter the number of bulbs (M): "))
    bulbs = []
    # For each bulb, read the number of connected switches, their indices, and required parity
    for i in range(M):
        k = int(input(f"Enter the number of connected switches for bulb {i + 1} (k): "))
        # Input validation for switch indices
        while True:
            try:
                # Strip whitespace and split by comma
                switches = list(map(int, input(f"Enter the connected switch indices for bulb {i + 1} (comma-separated): ").strip().split(',')))
                if all(1 <= switch <= N for switch in switches):
                    break
                else:
                    print(f"Invalid switch indices. Please enter indices between 1 and {N}.")
            except ValueError:
                print("Invalid input. Please enter integer values separated by commas.")
        # Read the required parity for the bulb with validation
        while True:
            try:
                parity = int(input(f"Enter the required parity for bulb {i + 1} (0 for even, 1 for odd): "))
                if parity in [0, 1]:
                    break
                print("Invalid parity. Please enter 0 for even or 1 for odd.")
            except ValueError:
                print("Invalid input. Please enter 0 or 1.")
        bulbs.append(Bulb(k, switches, parity))
    total_combinations = 0
    # Generate all possible combinations of switch states
    for i in range(2 ** N):
        switch_states = [(i >> j) & 1 for j in range(N)]
        # Check if all bulbs are valid for the current combination of switch states
        if all(bulb.is_valid(switch_states) for bulb in bulbs):
            total_combinations += 1
    # Print the total count of valid combinations
    print(f"Total valid combinations: {total_combinations}")
if __name__ == "__main__":
    main()