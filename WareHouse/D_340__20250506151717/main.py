'''
Main application file for the stage time calculator.
'''
from collections import deque
from input_frame import InputFrame
from output_frame import OutputFrame
class MainApp:
    def __init__(self, master):
        self.master = master
        master.title("Stage Time Calculator")
        self.input_frame = InputFrame(master, self.calculate_min_time)
        self.input_frame.pack()
        self.output_frame = OutputFrame(master)
        self.output_frame.pack()
    def calculate_min_time(self):
        N, A, B, X = self.input_frame.get_input()
        if N is None or A is None or B is None or X is None:
            self.output_frame.display_result("Invalid input. Please check your values.")
            return
        min_time = [float('inf')] * (N + 1)
        min_time[1] = 0
        queue = deque([1])  # Start from stage 1
        while queue:
            i = queue.popleft()
            # Update min_time for moving to the next stage using action A
            if i < N:  # Ensure we do not exceed the bounds
                if min_time[i + 1] > min_time[i] + A[i - 1]:  # Access A[i-1]
                    min_time[i + 1] = min_time[i] + A[i - 1]
                    queue.append(i + 1)  # Add to queue for further processing
            # Update min_time for jumping to stage X[i-1] using action B
            if i < N - 1:  # Ensure we do not exceed the bounds
                if 1 <= X[i - 1] <= N:  # Check if X[i-1] is a valid stage
                    if min_time[X[i - 1]] > min_time[i] + B[i - 1]:  # Access B[i-1]
                        min_time[X[i - 1]] = min_time[i] + B[i - 1]
                        queue.append(X[i - 1])  # Add to queue for further processing
        if min_time[N] == float('inf'):
            self.output_frame.display_result("No valid path to reach stage N.")
        else:
            self.output_frame.display_result(f"Minimum time to reach stage {N}: {min_time[N]} seconds")
if __name__ == "__main__":
    import tkinter as tk
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()