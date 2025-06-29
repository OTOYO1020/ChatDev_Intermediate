'''
Defines the Switch class to represent each switch and its state.
'''
class Switch:
    def __init__(self, index):
        self.index = index
        self.state = False  # Initially off
    def turn_on(self):
        self.state = True
    def turn_off(self):
        self.state = False