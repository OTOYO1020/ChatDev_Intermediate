'''
Main application file for Santa's movement simulation.
'''
from santa_simulation import find_final_position_and_houses
def main():
    # Input handling
    N = int(input("Enter the number of houses (N): "))
    houses = eval(input("Enter the houses as a list of tuples (e.g., [(1, 2), (3, 4)]): "))
    M = int(input("Enter the number of movements (M): "))
    movements = eval(input("Enter the movements as a list of tuples (e.g., [('U', 2), ('R', 3)]): "))
    S = eval(input("Enter the starting position as a tuple (e.g., (0, 0)): "))
    # Validate input
    if not isinstance(houses, list) or not all(isinstance(h, tuple) and len(h) == 2 for h in houses):
        print("Invalid houses input. Please provide a list of tuples.")
        return
    if not isinstance(movements, list) or not all(isinstance(m, tuple) and len(m) == 2 for m in movements):
        print("Invalid movements input. Please provide a list of tuples.")
        return
    final_position, distinct_houses_count = find_final_position_and_houses(N, houses, M, movements, S)
    # Output the results
    print(f"Final Position: {final_position}")
    print(f"Distinct Houses Count: {distinct_houses_count}")
if __name__ == "__main__":
    main()