'''
Main entry point for the bus passenger tracking application.
'''
from bus_passenger_tracker import BusPassengerTracker
if __name__ == "__main__":
    tracker = BusPassengerTracker()
    N = int(input("Enter the number of stops: "))
    for i in range(N):
        A_i = int(input(f"Enter change in passengers for stop {i + 1}: "))
        tracker.update_passengers(A_i)
    min_passengers = tracker.get_min_passengers()
    print(f"Minimum possible current number of passengers: {min_passengers}")