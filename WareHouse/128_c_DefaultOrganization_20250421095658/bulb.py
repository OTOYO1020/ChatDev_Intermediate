'''
Defines the Bulb class to represent each bulb and its properties.
'''
class Bulb:
    def __init__(self, connected_switches, required_parity):
        self.connected_switches = connected_switches
        self.required_parity = required_parity