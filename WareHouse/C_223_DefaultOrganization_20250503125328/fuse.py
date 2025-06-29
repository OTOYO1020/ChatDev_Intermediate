'''
Module to define Fuse and FuseCalculator classes for calculating the meeting point of flames.
'''
class Fuse:
    def __init__(self, length, burn_speed):
        self.length = length
        self.burn_speed = burn_speed
class FuseCalculator:
    def __init__(self):
        self.fuses = []
    def add_fuse(self, length, burn_speed):
        fuse = Fuse(length, burn_speed)
        self.fuses.append(fuse)
    def calculate_meeting_point(self):
        left_time = 0
        right_time = 0
        total_length = sum(fuse.length for fuse in self.fuses)
        left_index = 0
        right_index = len(self.fuses) - 1
        while left_index <= right_index:
            if left_time < right_time:
                left_time += self.fuses[left_index].length / self.fuses[left_index].burn_speed
                left_index += 1
            else:
                right_time += self.fuses[right_index].length / self.fuses[right_index].burn_speed
                right_index -= 1
        # Calculate the meeting point based on the last updated left_index and right_index
        if left_time < right_time:
            # Calculate position from the left
            position = sum(fuse.length for fuse in self.fuses[:left_index]) + (right_time - left_time) * self.fuses[left_index - 1].burn_speed
        elif right_time < left_time:
            # Calculate position from the right
            position = total_length - sum(fuse.length for fuse in self.fuses[right_index + 1:]) - (left_time - right_time) * self.fuses[right_index + 1].burn_speed
        else:
            # If both times are equal, the meeting point is at the end of the last fuse
            return total_length
        # Ensure the position is returned as an integer
        return int(position)