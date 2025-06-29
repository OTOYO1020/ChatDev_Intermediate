'''
Module for counting balls based on their occurrences.
'''
from typing import List
class BallCounter:
    def __init__(self):
        self.count = {}
        self.total_balls = 0
    def count_balls_after_insertion(self, N: int, a: List[int]) -> List[int]:
        '''
        Count the number of balls remaining after each insertion based on their occurrences.
        When a ball's count reaches 2, all instances of that ball disappear.
        '''
        result = []
        self.total_balls = 0  # Initialize total balls at the start of the method
        for i in range(N):
            ball = a[i]
            if ball in self.count:
                # Increment the count of the ball
                self.count[ball] += 1
                # If the count of the ball is now 2, we need to remove all instances
                if self.count[ball] == 2:
                    self.total_balls -= self.count[ball]  # Remove all instances of this ball
                    self.count[ball] = 0  # Reset the count to 0 since all instances are removed
                else:
                    self.total_balls -= 1  # Remove one instance for each additional count
            else:
                self.count[ball] = 1
                self.total_balls += 1  # Increment total for new ball
            # Append the current total number of balls to the result
            result.append(self.total_balls)
        return result