'''
Main entry point for the restaurant sorting application.
'''
from restaurant import RestaurantManager
def main():
    N = int(input("Enter the number of restaurants: "))
    manager = RestaurantManager()
    manager.set_number_of_restaurants(N)
    for i in range(1, N + 1):
        city, score = input(f"Enter city name and score for restaurant {i} (separated by space): ").split()
        score = int(score)
        manager.add_restaurant(city, score)
    manager.sort_restaurants()
    sorted_ids = manager.get_sorted_ids()
    print("Sorted restaurant IDs:", ' '.join(map(str, sorted_ids)))
if __name__ == "__main__":
    main()