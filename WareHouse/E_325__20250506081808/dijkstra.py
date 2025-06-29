'''
Dijkstra's algorithm implementation for finding the shortest path in a graph.
'''
import heapq
import math
class DijkstraAlgorithm:
    def __init__(self, N, A, B, C, D):
        self.N = N
        self.A = A
        self.B = B
        self.C = C
        self.D = D
    def find_shortest_path(self):
        min_time = [math.inf] * self.N
        min_time[0] = 0  # Starting city (city 1)
        priority_queue = [(0, 0)]  # (time, city index)
        while priority_queue:
            current_time, current_city = heapq.heappop(priority_queue)
            if current_time > min_time[current_city]:
                continue
            for next_city in range(self.N):
                if next_city != current_city:
                    time_car = self.D[current_city][next_city] * self.A
                    time_train = self.D[current_city][next_city] * self.B + self.C
                    # Update min_time for company car
                    if min_time[next_city] > current_time + time_car:
                        min_time[next_city] = current_time + time_car
                        heapq.heappush(priority_queue, (min_time[next_city], next_city))
                    # Update min_time for train
                    if min_time[next_city] > current_time + time_train:
                        min_time[next_city] = current_time + time_train
                        heapq.heappush(priority_queue, (min_time[next_city], next_city))
                    # Allow switching from company car to train without penalty
                    if min_time[next_city] > current_time + time_train:
                        min_time[next_city] = current_time + time_train
                        heapq.heappush(priority_queue, (min_time[next_city], next_city))
                    # Allow switching from train to company car without penalty
                    if min_time[next_city] > current_time + time_car:
                        min_time[next_city] = current_time + time_car
                        heapq.heappush(priority_queue, (min_time[next_city], next_city))
        return min_time[self.N - 1]  # Return the minimum time to reach city N