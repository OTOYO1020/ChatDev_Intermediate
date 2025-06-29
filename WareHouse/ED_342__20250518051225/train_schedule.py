'''
Module for managing train schedules and calculating latest arrival times.
'''
from typing import List, Tuple
class TrainSchedule:
    def __init__(self, N: int, M: int, train_info: List[Tuple[int, int, int, int, int, int]]):
        self.N = N
        self.M = M
        self.train_info = train_info
        self.schedules = self.create_schedules()
    def create_schedules(self):
        '''
        Create a dictionary to store train schedules based on the provided train information.
        '''
        schedules = {}
        for l, d, k, c, A, B in self.train_info:
            if l not in schedules:
                schedules[l] = []
            schedules[l].append((d, k, c, A, B))
        return schedules
    def calculate_latest_arrival_times(self) -> List[int]:
        '''
        Calculate the latest arrival times for each station from 1 to N-1.
        Returns a list of integers representing the latest arrival times.
        '''
        latest_arrivals = [-float('inf')] * self.N
        latest_arrivals[0] = 0  # Starting point at station 1
        for station in range(1, self.N):
            if station in self.schedules:
                for d, k, c, A, B in self.schedules[station]:
                    # Check if we can transfer from the previous station
                    if station - 1 in self.schedules:  # Check if previous station has schedules
                        for prev_d, prev_k, prev_c, prev_A, prev_B in self.schedules[station - 1]:
                            # Updated condition for valid transfer
                            if latest_arrivals[station - 1] != -float('inf') and prev_B <= d and prev_A <= d:
                                latest_arrivals[station] = max(latest_arrivals[station], B)
        # Replace -inf with -1 for stations that cannot be reached
        for i in range(1, self.N):
            if latest_arrivals[i] == -float('inf'):
                latest_arrivals[i] = -1  # No valid train sequence
        return latest_arrivals[1:]  # Return results for stations 1 to N-1