'''
Module containing the Bulb class for managing bulb properties and validation.
'''
class Bulb:
    def __init__(self, k, switches, parity):
        self.k = k
        self.switches = switches
        self.parity = parity
    def is_valid(self, switch_states):
        # Adjust switch indices to be 0-based and count the number of on switches
        if self.k == 0:  # No connected switches
            return False  # No bulb can be lit without connected switches
        on_count = sum(switch_states[switch_index - 1] for switch_index in self.switches)
        # Check if the count of on switches matches the required parity
        return on_count % 2 == self.parity