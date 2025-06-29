'''
Defines the Bulb class that represents a bulb with its connected switches and required parity.
'''
class Bulb:
    def __init__(self, connected_switches, required_parity):
        self.connected_switches = connected_switches
        self.required_parity = required_parity