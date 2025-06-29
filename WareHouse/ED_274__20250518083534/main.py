'''
Main application file for the Takahashi Travel application.
'''
from utils import get_input, calculate_shortest_time
def main():
    try:
        N = int(input("Enter the number of towns: "))
        M = int(input("Enter the number of chests: "))
        towns, chests = get_input(N, M)
        shortest_time = calculate_shortest_time(N, M, towns, chests)
        print(f"Shortest Time: {shortest_time:.2f}")
    except ValueError:
        print("Input Error: Please enter valid integers for towns and chests.")
if __name__ == "__main__":
    main()