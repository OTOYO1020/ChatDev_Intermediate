'''
Main application file for the Bulb Switch application.
'''
from bulb_switch import count_valid_combinations
def read_switches(N, bulb_index):
    while True:
        try:
            k_i = int(input(f"Enter number of switches for bulb {bulb_index + 1}: "))
            if k_i < 1 or k_i > N:
                print(f"Number of switches must be between 1 and {N}.")
                continue
            switches = list(map(int, input(f"Enter {k_i} switch numbers for bulb {bulb_index + 1} (space-separated): ").split()))
            if len(switches) != k_i:
                print(f"You must enter exactly {k_i} switch numbers.")
                continue
            if any(s < 1 or s > N for s in switches):
                print(f"Switch numbers for bulb {bulb_index + 1} must be between 1 and {N}.")
                continue
            if len(set(switches)) != len(switches):
                print(f"Switch numbers for bulb {bulb_index + 1} must be unique.")
                continue
            return switches
        except ValueError:
            print("Invalid input. Please enter integers only.")
def main():
    # Read integers N and M from standard input
    N, M = map(int, input("Enter number of switches (N) and bulbs (M): ").split())
    bulb_conditions = []
    # Read conditions for each bulb
    for i in range(M):
        switches = read_switches(N, i)
        # Read the integer p_i, the required parity
        while True:
            try:
                p_i = int(input(f"Enter required parity for bulb {i + 1} (0 or 1): "))
                if p_i not in (0, 1):
                    print("Invalid input. Please enter 0 or 1 for the required parity.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter 0 or 1 for the required parity.")
        # Store the tuple in bulb_conditions
        bulb_conditions.append((*switches, p_i))
    # Calculate valid combinations
    valid_count = count_valid_combinations(N, bulb_conditions)
    print(f"Total valid combinations: {valid_count}")
if __name__ == "__main__":
    main()