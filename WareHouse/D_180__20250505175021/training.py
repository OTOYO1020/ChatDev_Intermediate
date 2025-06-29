'''
Contains the training logic for the simulation.
'''
class TrainingSimulator:
    '''
    Class to simulate the training process.
    '''
    def __init__(self, x, y, a, b):
        '''
        Initializes the training simulator with parameters.
        '''
        self.strength = x
        self.max_strength = y
        self.a = a
        self.b = b
        self.exp = 0
    def simulate_training(self):
        '''
        Simulates the training process until the strength reaches or exceeds the maximum.
        '''
        while self.strength < self.max_strength:
            new_str_kakomon = self.strength * self.a
            new_str_atcoder = self.strength + self.b
            # Check if both options are valid
            if new_str_kakomon < self.max_strength and new_str_atcoder < self.max_strength:
                # Choose the option that maximizes the potential for future training
                if (new_str_kakomon * self.a < self.max_strength) and (new_str_kakomon > new_str_atcoder):
                    self.strength = new_str_kakomon
                else:
                    self.strength = new_str_atcoder
                self.exp += 1  # Increment EXP after a valid update
            elif new_str_kakomon < self.max_strength:
                self.strength = new_str_kakomon
                self.exp += 1  # Increment EXP after a valid update
            elif new_str_atcoder < self.max_strength:
                self.strength = new_str_atcoder
                self.exp += 1  # Increment EXP after a valid update
            else:
                break  # If neither option is valid, break the loop
        return self.exp