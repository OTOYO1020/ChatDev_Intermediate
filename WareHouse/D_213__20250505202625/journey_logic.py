'''
Contains the logic for simulating the journey through cities.
'''
class JourneyLogic:
    def __init__(self, num_cities):
        self.num_cities = num_cities
        self.roads = [[] for _ in range(num_cities + 1)]
        self.visited = [False] * (num_cities + 1)
    def add_road(self, city_a, city_b):
        self.roads[city_a].append(city_b)
        self.roads[city_b].append(city_a)
    def simulate_journey(self):
        visited_sequence = []
        if self.num_cities == 1:  # Handle the case of a single city
            visited_sequence.append(1)
            return visited_sequence
        stack = [1]
        self.visited[1] = True
        visited_sequence.append(1)  # Append the starting city to the visited sequence
        while stack:
            current_city = stack[-1]
            unvisited_cities = [city for city in sorted(self.roads[current_city]) if not self.visited[city]]
            if unvisited_cities:
                next_city = unvisited_cities[0]
                stack.append(next_city)
                self.visited[next_city] = True
                visited_sequence.append(next_city)  # Append the next city when visiting
            else:
                if current_city == 1:
                    break  # End the journey if currently in City 1
                stack.pop()  # Backtrack
        return visited_sequence