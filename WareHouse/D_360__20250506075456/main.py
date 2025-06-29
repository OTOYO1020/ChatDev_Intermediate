'''
Main application file for the Ant Simulation.
'''
from ant_simulation import calculate_final_positions, count_passes
def main():
    try:
        N = int(input("Enter the number of ants (N):\n").strip())
        T = float(input("Enter the time (T):\n").strip())
        if T < 0:
            raise ValueError("Time (T) must be a non-negative value.")
        S = input("Enter the binary string S (length N, indexed from 0):\n").strip()
        if len(S) != N or any(char not in '01' for char in S):
            raise ValueError(f"Binary string S must be of length {N} and contain only '0' and '1'.")
        while True:
            try:
                X = list(map(float, input(f"Enter {N} space-separated coordinates for X (indexed from 0):\n").strip().split()))
                if len(X) != N:
                    raise ValueError(f"Expected {N} coordinates, but got {len(X)}.")
                break  # Exit the loop if input is valid
            except ValueError:
                print("Invalid input for coordinates. Please enter valid numbers separated by spaces.")
        final_positions = calculate_final_positions(N, T, S, X)
        pass_count = count_passes(final_positions)
        print(f"The number of passes is: {pass_count}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()