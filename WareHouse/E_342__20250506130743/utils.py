'''
Utility module to calculate the latest arrival time at station N from station S.
'''
from collections import deque
def calculate_latest_arrival(S, train_info, N):
    latest_time = [float('-inf')] * (N + 1)  # Initialize latest arrival times for all stations
    latest_time[S] = 0  # Start from station S with arrival time 0
    queue = deque([S])  # Use a queue to explore stations
    while queue:
        current_station = queue.popleft()
        current_arrival_time = latest_time[current_station]
        # Check for all trains to see if we can take them from the current station
        for train in train_info:
            # Check if the train departs from the current station
            if train.d_i == current_station:
                # Ensure we arrive at the departure station before the train departs
                if current_arrival_time <= train.c_i and current_arrival_time <= train.A_i:
                    new_arrival_time = train.B_i
                    # Update latest arrival time only if it's greater than the previously recorded time
                    if latest_time[train.k_i] < new_arrival_time:
                        latest_time[train.k_i] = new_arrival_time  # Update latest arrival time
                        queue.append(train.k_i)  # Continue to explore from this station
            # Check if we can arrive at the current station using other trains
            if train.k_i == current_station:
                # If we arrive at the current station, we can check for other trains departing from here
                if latest_time[train.d_i] < train.B_i:
                    latest_time[train.d_i] = train.B_i
                    queue.append(train.d_i)  # Explore from the new station
    # Return the latest arrival time at station N, or -1 if unreachable
    return latest_time[N] if latest_time[N] != float('-inf') else -1