'''
Module implementing Dijkstra's algorithm to calculate minimum travel time.
'''
from typing import List
import heapq
def minimum_travel_time(N: int, A: int, B: int, C: int, D: List[List[int]]) -> int:
    # Validate distance matrix dimensions
    if len(D) != N or any(len(row) != N for row in D):
        raise ValueError("Distance matrix must be square with dimensions N x N.")
    # Validate distance matrix values
    for row in D:
        if any(distance < 0 for distance in row):
            raise ValueError("Distance matrix must contain non-negative values.")
    # Initialize the priority queue and the minimum travel times
    pq = [(0, 0, 'car')]  # (travel_time, city_index, last_mode)
    min_time = [[float('inf'), float('inf')] for _ in range(N)]  # [car_time, train_time]
    min_time[0][0] = 0  # Starting point (city 1) with car
    while pq:
        current_time, current_city, last_mode = heapq.heappop(pq)
        # Skip processing if the current time is not optimal
        if last_mode == 'car' and current_time > min_time[current_city][0]:
            continue
        if last_mode == 'train' and current_time > min_time[current_city][1]:
            continue
        # If we reach city N, return the travel time
        if current_city == N - 1:
            return current_time
        # Explore neighbors
        for neighbor in range(N):
            if neighbor != current_city and D[current_city][neighbor] > 0:  # Only consider valid paths
                # Calculate travel time using company car
                car_time = current_time + D[current_city][neighbor] * A
                # Update car time if it's better than the previously recorded time
                if car_time < min_time[neighbor][0]:
                    min_time[neighbor][0] = car_time
                    heapq.heappush(pq, (car_time, neighbor, 'car'))
                # Calculate travel time using train
                train_time = current_time + D[current_city][neighbor] * B
                # Allow switching from car to train without cost
                if train_time < min_time[neighbor][1]:
                    min_time[neighbor][1] = train_time
                    heapq.heappush(pq, (train_time, neighbor, 'train'))
    # Return the minimum time to reach city N, or -1 if unreachable
    return min(min_time[N - 1]) if min(min_time[N - 1]) != float('inf') else -1