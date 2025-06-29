'''
Main entry point for the travel cost calculator application.
'''
from travel_cost_calculator import TravelCostCalculator
from city import City
def main():
    N = int(input("Enter the number of cities: "))
    calculator = TravelCostCalculator()
    for i in range(N):
        attempts = 0
        while attempts < 3:  # Limit to 3 attempts
            try:
                coordinates = input(f"Enter coordinates for city {i + 1} (format: X,Y,Z): ")
                x, y, z = map(int, coordinates.split(","))
                city = City(x, y, z)
                calculator.cities.append(city)
                break  # Exit the loop if input is valid
            except ValueError:
                attempts += 1
                print(f"Invalid input. Please enter coordinates in the format X,Y,Z (e.g., 1,2,3). Attempts left: {3 - attempts}")
        if attempts == 3:
            print("Maximum attempts reached. Exiting the program.")
            return  # Exit the program if maximum attempts are reached
    min_cost = calculator.find_min_cost()
    print(f"Minimum Travel Cost: {min_cost}")
if __name__ == "__main__":
    main()