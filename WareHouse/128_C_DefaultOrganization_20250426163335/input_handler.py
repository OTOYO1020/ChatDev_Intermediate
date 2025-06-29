'''
Handles user input for the number of switches, bulbs, and their connections.
'''
from bulb import Bulb
class InputHandler:
    def __init__(self, app):
        self.app = app
        self.switch_count = 0
        self.bulbs = []
    def get_input(self):
        self.switch_count = int(input("Enter number of switches: "))
        bulb_count = int(input("Enter number of bulbs: "))
        self.bulbs = []
        for i in range(bulb_count):
            k_i = int(input(f"Enter number of connected switches for bulb {i + 1}: "))  # Read k_i
            while True:
                try:
                    connected_switches = list(map(int, input(f"Enter connected switches for bulb {i + 1} (space-separated, starting from 1): ").split()))
                    if len(connected_switches) == k_i and all(1 <= s <= self.switch_count for s in connected_switches):
                        break
                    else:
                        print(f"Error: You must enter exactly {k_i} connected switches within the range 1 to {self.switch_count}. Please try again.")
                except ValueError:
                    print("Error: Please enter valid integers for connected switches.")
            required_parity = int(input(f"Enter required parity for bulb {i + 1} (0 or 1): "))
            while required_parity not in (0, 1):
                print("Error: Required parity must be either 0 or 1. Please try again.")
                required_parity = int(input(f"Enter required parity for bulb {i + 1} (0 or 1): "))
            # Adjust for zero-based indexing if needed
            connected_switches = [s - 1 for s in connected_switches]  # Convert to zero-based index
            self.bulbs.append(Bulb(connected_switches, required_parity))
        self.app.bulbs = self.bulbs  # Pass the bulbs to the main app