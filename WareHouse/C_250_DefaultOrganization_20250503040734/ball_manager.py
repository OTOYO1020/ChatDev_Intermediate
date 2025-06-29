'''
Module for managing the state of the balls.
'''
class BallManager:
    def __init__(self, n):
        self.balls = list(range(1, n + 1))
    def swap_balls(self, x):
        """
        Swap the position of the ball with value x in the balls array.
        If x is found at the last index, swap with the previous index.
        If x is found at any other index, swap with the next index.
        If x is not found, print a warning message and skip the operation.
        """
        if x < 1 or x > len(self.balls):
            raise ValueError(f"Ball with value {x} is out of valid range (1 to {len(self.balls)}). Cannot perform swap operation.")
        if x not in self.balls:
            print(f"Warning: Ball with value {x} not found. Skipping operation.")
            return  # Skip the operation if the ball is not found
        index = self.balls.index(x)
        # Check if there is only one ball, in which case no swap is needed
        if len(self.balls) == 1:
            return
        if index < len(self.balls) - 1:
            # Swap with the next ball
            self.balls[index], self.balls[index + 1] = self.balls[index + 1], self.balls[index]
        elif index == len(self.balls) - 1 and index > 0:
            # Swap with the previous ball if at the last index and not the first
            self.balls[index], self.balls[index - 1] = self.balls[index - 1], self.balls[index]