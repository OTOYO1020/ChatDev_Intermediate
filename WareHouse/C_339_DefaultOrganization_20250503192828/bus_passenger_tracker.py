'''
This module contains the BusPassengerTracker class to manage passenger counts.
'''
class BusPassengerTracker:
    def __init__(self):
        self.current_passengers = 0
        self.min_passengers = float('inf')  # Initialize to infinity to track minimum passengers correctly
    def update_passengers(self, change):
        self.current_passengers += change
        # Update min_passengers to the lowest point reached by current_passengers
        if self.current_passengers < self.min_passengers:
            self.min_passengers = self.current_passengers
    def get_min_passengers(self):
        return max(0, -self.min_passengers) if self.min_passengers != float('inf') else 0  # Ensure non-negative passengers