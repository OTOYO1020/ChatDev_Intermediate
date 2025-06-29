'''
Module for calculating the minimum number of problems to solve for each player.
'''
from typing import List
def is_valid_problem_index(index: int, M: int) -> bool:
    return 0 <= index < M
def calculate_min_problems_to_solve(N: int, M: int, scores: List[int], solved: List[str]) -> List[int]:
    total_scores = []
    invalid_inputs = []  # To track invalid inputs for reporting
    # Calculate total scores for each player
    for i in range(N):
        total_score = scores[i] + i  # Adding bonus score (player index)
        if solved[i].strip():  # Check if the player has solved any problems
            for problem in solved[i].split(','):
                problem_index = problem.strip()
                if not problem_index:  # Skip empty entries
                    continue
                try:
                    problem_index = int(problem_index)
                    if not is_valid_problem_index(problem_index, M):
                        invalid_inputs.append(f"Invalid problem index {problem_index} for player {i}. Must be between 0 and {M-1}.")
                        continue  # Skip invalid index
                    total_score += scores[problem_index]
                except ValueError:
                    invalid_inputs.append(f"Invalid input '{problem}' for player {i}. Must be a valid integer.")
                    continue  # Skip invalid input
        total_scores.append(total_score)
    # Report invalid inputs if any
    if invalid_inputs:
        return invalid_inputs  # Return invalid inputs to be displayed in the GUI
    results = []
    # Calculate the minimum number of problems to solve for each player
    for i in range(N):
        target_score = max(total_scores[j] for j in range(N) if j != i)
        # If current score is already greater than target score, no problems need to be solved
        if total_scores[i] > target_score:
            results.append(0)
            continue
        # Check for unsolved problems
        unsolved_scores = [scores[j] for j in range(M) if str(j) not in solved[i].split(',')]
        # If no unsolved problems, append 0
        if not unsolved_scores:
            results.append(0)  # No problems to solve
            continue
        unsolved_scores.sort(reverse=True)  # Sort unsolved scores in descending order
        current_score = total_scores[i]
        problems_needed = 0
        for score in unsolved_scores:
            if current_score > target_score:
                break
            current_score += score
            problems_needed += 1
        if current_score <= target_score:
            problems_needed = len(unsolved_scores)  # Return total unsolved problems if not possible to exceed
        results.append(problems_needed)
    return results