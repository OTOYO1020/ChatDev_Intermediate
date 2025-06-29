'''
Module to calculate travel costs and solve the Traveling Salesman Problem.
'''
from city import City
class TravelCostCalculator:
    def __init__(self):
        self.cities = []
        self.memo = {}
    def travel_cost(self, city_a: City, city_b: City) -> int:
        '''
        Calculate the travel cost between two cities using the formula:
        |X_b - X_a| + |Y_b - Y_a| + max(0, Z_b - Z_a).
        '''
        x_a, y_a, z_a = city_a.get_coordinates()  # Use the new method
        x_b, y_b, z_b = city_b.get_coordinates()  # Use the new method
        return abs(x_b - x_a) + abs(y_b - y_a) + max(0, z_b - z_a)
    def tsp(self, current_index: int, visited_mask: int) -> int:
        '''
        Recursive function to explore all possible routes and calculate the minimum travel cost.
        Uses memoization to optimize the recursive calls.
        '''
        if visited_mask == (1 << len(self.cities)) - 1:
            return self.travel_cost(self.cities[current_index], self.cities[0])
        if (current_index, visited_mask) in self.memo:
            return self.memo[(current_index, visited_mask)]
        min_cost = float('inf')
        for next_index in range(len(self.cities)):
            if visited_mask & (1 << next_index) == 0:
                cost = self.travel_cost(self.cities[current_index], self.cities[next_index])
                total_cost = cost + self.tsp(next_index, visited_mask | (1 << next_index))
                min_cost = min(min_cost, total_cost)
        self.memo[(current_index, visited_mask)] = min_cost
        return min_cost
    def find_min_cost(self) -> int:
        '''
        Clear the memoization dictionary and start the TSP traversal from City 1.
        '''
        self.memo.clear()
        return self.tsp(0, 1)  # Start with index 0 for City 1