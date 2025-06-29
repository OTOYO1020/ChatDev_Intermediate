'''
This module defines the SnakeQueue class to manage the queue of snakes.
'''
class SnakeQueue:
    def __init__(self):
        self.queue = []
        self.head_position = 0
    def add_snake(self, length):
        self.queue.append(length)
        # Update head_position to the total length of all snakes in the queue
        if len(self.queue) == 1:
            self.head_position = 0  # First snake's head position is 0
        else:
            self.head_position += length  # Update head position based on the last snake added
    def remove_snake(self):
        if self.queue:
            m = self.queue.pop(0)  # Remove the first snake
            for i in range(len(self.queue)):
                self.queue[i] -= m  # Decrease the head position of remaining snakes
            # Update head_position to the head of the new first snake
            if self.queue:
                self.head_position = sum(self.queue[:1])  # Head position of the new first snake
            else:
                self.head_position = 0  # Reset to 0 if no snakes are left
    def get_head_position(self, k):
        if 0 < k <= len(self.queue):
            position = sum(self.queue[:k])  # Calculate head position of the k-th snake
            return position
        return None