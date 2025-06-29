'''
Main application file for the submission processing.
'''
from input_frame import InputFrame
from result_frame import ResultFrame
import tkinter as tk
class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Submission Results Calculator")
        self.input_frame = InputFrame(self.root, self.calculate_results)
        self.input_frame.pack(pady=10)
        self.result_frame = ResultFrame(self.root)
        self.result_frame.pack(pady=10)
        self.root.mainloop()
    def calculate_results(self, N: int, M: int):
        submissions = self.input_frame.get_submissions()
        # Validate the number of submissions
        if len(submissions) > M:
            raise ValueError(f"Number of submissions exceeds the limit of {M}.")
        correct_answers = set()
        penalties = {}
        for submission in submissions:
            problem_id, verdict = submission  # Unpack the tuple
            # Validate the problem_id
            if problem_id > N:
                raise ValueError(f"Problem ID {problem_id} exceeds the limit of {N}.")
            # Validate the verdict
            if verdict not in ['AC', 'WA']:
                print(f"Invalid verdict '{verdict}' for problem ID {problem_id}. Skipping this submission.")
                continue  # Skip invalid submissions
            if verdict == 'AC':
                correct_answers.add(problem_id)
                # If the problem is solved correctly, reset penalties for that problem
                if problem_id in penalties:
                    del penalties[problem_id]  # Remove penalties for this problem
            else:  # verdict == 'WA'
                if problem_id not in penalties:
                    penalties[problem_id] = 0
                if problem_id not in correct_answers:  # Only count WA if no AC has been received
                    penalties[problem_id] += 1  # Increment penalty for WA
        total_correct = len(correct_answers)
        total_penalties = sum(penalties[pid] for pid in correct_answers if pid in penalties)  # Corrected line
        # Return the results as a tuple
        return total_correct, total_penalties
if __name__ == "__main__":
    MainApp()