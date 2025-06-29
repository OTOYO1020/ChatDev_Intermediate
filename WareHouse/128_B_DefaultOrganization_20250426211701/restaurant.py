'''
Module containing the Restaurant and RestaurantManager classes.
'''
class Restaurant:
    def __init__(self, city, score, id):
        self.city = city
        self.score = score
        self.id = id
class RestaurantManager:
    def __init__(self):
        self.restaurants = []
        self.restaurant_id_counter = 1  # Initialize a counter for restaurant IDs
        self.max_restaurants = 0  # Track the maximum number of restaurants
    def set_number_of_restaurants(self, max_restaurants):
        self.max_restaurants = max_restaurants
        self.restaurants = []  # Clear the existing restaurants
        self.restaurant_id_counter = 1  # Reset the counter to 1 for new entries
    def add_restaurant(self, city, score):  # Accept only city and score as parameters
        if self.max_restaurants == 0:
            print("Please set the number of restaurants first.")
            return  # Exit the method if the limit is not set
        if len(self.restaurants) >= self.max_restaurants:
            print("Maximum number of restaurants reached. Cannot add more.")
            return  # Exit the method if the limit is reached
        if not city.strip():  # Validate city name
            print("City name cannot be empty.")
            return  # Exit if city name is invalid
        new_restaurant = Restaurant(city, score, self.restaurant_id_counter)
        self.restaurants.append(new_restaurant)
        self.restaurant_id_counter += 1  # Increment the counter for the next restaurant
    def sort_restaurants(self):
        self.restaurants.sort(key=lambda r: (r.city, -r.score))
    def get_sorted_ids(self):
        return [restaurant.id for restaurant in self.restaurants]