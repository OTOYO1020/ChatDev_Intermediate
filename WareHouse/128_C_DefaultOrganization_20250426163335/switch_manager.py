'''
Manages the states of switches and checks the validity of combinations.
'''
from bulb import Bulb
class SwitchManager:
    def __init__(self):
        self.switch_count = 0
        self.bulbs = []
    def initialize(self, switch_count, bulbs):
        self.switch_count = switch_count
        self.bulbs = bulbs
    def calculate_valid_combinations(self):
        valid_count = 0
        total_combinations = 1 << self.switch_count  # 2^N combinations
        for i in range(total_combinations):
            if self.check_bulbs(i):
                valid_count += 1
        return valid_count
    def check_bulbs(self, switch_state):
        for bulb in self.bulbs:
            # If there are no connected switches, the bulb is always considered lit
            if len(bulb.connected_switches) == 0:
                continue  # Skip to the next bulb
            # Count the number of on switches connected to the bulb
            on_switches_count = sum((switch_state >> s) & 1 for s in bulb.connected_switches)
            if on_switches_count % 2 != bulb.required_parity:
                return False
        return True