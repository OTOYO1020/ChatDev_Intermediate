'''
Main entry point of the train schedule application.
'''
from train_schedule import TrainSchedule
from typing import List, Tuple
def main(N: int, M: int, train_info: List[Tuple[int, int, int, int, int, int]]) -> List[int]:
    train_schedule = TrainSchedule(N, M, train_info)
    latest_arrival_times = train_schedule.calculate_latest_arrival_times()
    return latest_arrival_times
if __name__ == "__main__":
    # Example input
    N = 4
    M = 5
    train_info = [
        (1, 0, 1, 1, 1, 2),
        (1, 1, 1, 1, 2, 3),
        (2, 2, 1, 1, 3, 4),
        (3, 3, 1, 1, 4, 5),
        (2, 1, 1, 1, 1, 3)
    ]
    result = main(N, M, train_info)
    print(result)