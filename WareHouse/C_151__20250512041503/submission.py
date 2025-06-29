'''
Module for handling submission entries.
'''
class SubmissionEntry:
    def __init__(self, problem_id: int, verdict: str):
        self.problem_id = int(problem_id)  # Ensure problem_id is treated as an integer
        self.verdict = verdict