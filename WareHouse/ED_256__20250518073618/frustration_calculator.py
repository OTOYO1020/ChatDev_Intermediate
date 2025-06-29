'''
Module to calculate the minimum possible sum of frustration based on dislikes.
'''
from typing import List, Tuple
from collections import defaultdict
import heapq
def min_frustration(N: int, dislikes: List[Tuple[int, int, int]]) -> int:
    # Create a graph to store dislikes and their associated costs
    graph = defaultdict(list)
    for person_a, person_b, cost in dislikes:
        graph[person_a].append((person_b, cost))
        graph[person_b].append((person_a, cost))
    # Initialize total frustration
    total_frustration = 0
    # Track the number of candies given to each person
    candies_given = [0] * N
    # Priority queue for processing people based on least frustration
    priority_queue = [(0, person) for person in range(N)]  # (frustration, person)
    heapq.heapify(priority_queue)
    while priority_queue:
        current_frustration, person = heapq.heappop(priority_queue)
        if candies_given[person] > 0:
            continue  # Skip if this person has already received a candy
        # Give candy to the current person
        candies_given[person] += 1
        total_frustration += current_frustration
        # Update frustration for disliked people
        for disliked, cost in graph[person]:
            if candies_given[disliked] == 0:  # If the disliked person hasn't received a candy
                # Update the frustration for the disliked person
                new_frustration = cost + current_frustration
                heapq.heappush(priority_queue, (new_frustration, disliked))
    return total_frustration