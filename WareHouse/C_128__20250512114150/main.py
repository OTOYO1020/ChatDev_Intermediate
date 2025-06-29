'''
Main application file for the Light Bulb Switches application.
'''
from light_bulb_logic import count_lighted_bulbs
from typing import List, Tuple
def main():
    """
    Main function to run the Light Bulb Switches application.
    It handles user input for the number of switches, bulbs, and their connections,
    and then calculates the number of valid combinations that light all bulbs.
    """
    # Input parsing
    N = int(input("Enter the number of switches (N): "))
    M = int(input("Enter the number of bulbs (M): "))
    connections = []
    while True:
        connections_input = input("Enter connections (format: switch1,switch2,...,parity; switch1,switch2,...,parity): ").strip()
        if not connections_input:
            print("No connections provided. Please enter at least one connection.")
            continue
        connections_input = connections_input.split(';')
        valid_input = True
        for conn in connections_input:
            parts = conn.strip().split(',')
            if len(parts) < 2:  # Ensure there's at least one switch and one parity
                print("Each connection must have at least one switch and a parity value.")
                valid_input = False
                break
            try:
                switches = list(map(int, parts[:-1]))
                if not switches:  # Check if the list of switches is empty
                    print("Switch list cannot be empty.")
                    valid_input = False
                    break
                parity = int(parts[-1])
                if parity not in (0, 1):  # Ensure parity is either 0 or 1
                    print("Parity must be 0 or 1.")
                    valid_input = False
                    break
                connections.append((switches, parity))
            except ValueError:
                print("Invalid input format. Please ensure switches are integers and parity is 0 or 1.")
                valid_input = False
                break
        if valid_input:
            break  # Exit the loop if input is valid
    result = count_lighted_bulbs(N, M, connections)
    print(f"Valid combinations: {result}")
if __name__ == "__main__":
    main()