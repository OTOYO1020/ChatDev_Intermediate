'''
Module containing the function to find work days based on input parameters.
'''
from typing import List
def find_work_days(N: int, K: int, C: int, S: str) -> List[int]:
    work_days = []  # List to store the days Takahashi will work
    cooldown_counter = 0  # Counter to track the cooldown period after selecting a workday
    for day in range(1, N + 1):
        # Check if the current day is marked as unavailable or in cooldown
        if S[day - 1] == 'x' or cooldown_counter > 0:
            if cooldown_counter > 0:
                cooldown_counter -= 1  # Decrease cooldown counter only if not working
            continue
        # If the current day is available for work and we haven't selected K workdays
        if len(work_days) < K:
            work_days.append(day)  # Add the current day to workdays
            cooldown_counter = C  # Set cooldown period after selecting a workday
        # If we have reached the maximum number of workdays, break early
        if len(work_days) == K:
            break
    return work_days