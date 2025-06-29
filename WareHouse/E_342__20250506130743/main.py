'''
Main application file for the Train Scheduler.
'''
from train_info import TrainInfo
from utils import calculate_latest_arrival
def main():
    # Read integers N and M from standard input
    try:
        N, M = map(int, input("Enter number of stations and train information (N M): ").split())
        if N <= 0 or M < 0:
            raise ValueError("N must be positive and M must be non-negative.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    train_info = []
    # Read M pieces of train information
    for _ in range(M):
        l_i, d_i, k_i, c_i, A_i, B_i = map(int, input("Enter train info (l_i, d_i, k_i, c_i, A_i, B_i): ").split())
        train_info.append(TrainInfo(l_i, d_i, k_i, c_i, A_i, B_i))
    # Calculate latest arrival times for each station S from 1 to N-1
    for s in range(1, N):
        result = calculate_latest_arrival(s, train_info, N)
        print(f"Latest arrival time from station {s} to station {N}: {result}")
if __name__ == "__main__":
    main()