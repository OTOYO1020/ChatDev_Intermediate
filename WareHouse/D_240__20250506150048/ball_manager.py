'''
Module to manage the balls in the cylinder.
'''
class BallManager:
    def __init__(self):
        self.balls = []  # Initialize an empty list to keep track of the balls
    def add_ball(self, value):
        '''
        Add a ball with the given value to the cylinder and check for consecutive occurrences.
        Parameters:
        value (int): The value of the ball to be added.
        '''
        self.balls.append(value)  # Append the new ball to the list
        self.check_consecutive()  # Check for and remove consecutive balls
    def check_consecutive(self):
        '''
        Check for consecutive occurrences of the same integer in the balls list.
        If there are 2 or more consecutive balls with the same value, remove them.
        '''
        if not self.balls:
            return  # If the list is empty, do nothing
        new_balls = []  # Temporary list to store valid balls
        count = 1  # Initialize count of consecutive balls
        last_ball = self.balls[0]  # Track the last ball value
        for i in range(1, len(self.balls)):
            if self.balls[i] == last_ball:
                count += 1  # Increment count if the same value is found
            else:
                if count < 2:  # Only add to new_balls if count is less than 2
                    new_balls.extend([last_ball] * count)  # Add the non-consecutive balls
                last_ball = self.balls[i]  # Update last_ball to the new value
                count = 1  # Reset count for the new value
        # Handle the last group of balls
        if count < 2:
            new_balls.extend([last_ball] * count)  # Add the last non-consecutive balls
        self.balls = new_balls  # Update the balls list with the valid balls
    def get_count(self):
        '''
        Get the current count of balls in the cylinder.
        Returns:
        int: The number of balls currently in the cylinder.
        '''
        return len(self.balls)  # Return the length of the balls list