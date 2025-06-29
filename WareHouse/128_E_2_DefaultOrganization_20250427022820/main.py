'''
Main application file for the Roadwork Distance Calculator.
'''
from tkinter import Tk, Label, Text, Button, END  # Added missing imports
from data_handler import merge_intervals, find_distance, populate_blocked_intervals
class RoadworkApp:
    def __init__(self, master):
        self.master = master
        master.title("Roadwork Distance Calculator")
        self.label = Label(master, text="Enter roadworks (X, S, T) and queries (D):")
        self.label.pack()
        self.text_area = Text(master, height=15, width=50)
        self.text_area.pack()
        self.submit_button = Button(master, text="Submit", command=self.submit_data)
        self.submit_button.pack()
        self.reset_button = Button(master, text="Reset", command=self.reset_data)  # Added reset button
        self.reset_button.pack()
        self.results_label = Label(master, text="Results:")
        self.results_label.pack()
        self.results_area = Text(master, height=10, width=50)
        self.results_area.pack()
    def submit_data(self):
        input_data = self.text_area.get("1.0", END).strip().splitlines()
        try:
            # Read N and Q from the first line of input
            N, Q = map(int, input_data[0].split())
            if N <= 0 or Q <= 0:
                raise ValueError("N and Q must be positive integers.")
            # Read roadworks and queries from the input
            roadworks = [tuple(map(int, line.split())) for line in input_data[1:N + 1]]
            queries = [int(line) for line in input_data[N + 1:N + 1 + Q]]
            # Validate roadworks and queries
            for roadwork in roadworks:
                if len(roadwork) != 3:
                    raise ValueError("Each roadwork must contain exactly three integers (X, S, T).")
            for query in queries:
                if not isinstance(query, int):
                    raise ValueError("Each query must be an integer.")
            # Populate blocked intervals from roadworks
            blocked_intervals = populate_blocked_intervals(roadworks)
            # Calculate distances for each query
            distances = [find_distance(D_i, blocked_intervals) for D_i in queries]
            self.display_results(distances)
        except Exception as e:
            self.results_area.delete("1.0", END)
            self.results_area.insert(END, f"Error: {str(e)}\n")
    def display_results(self, distances):
        self.results_area.delete("1.0", END)
        for distance in distances:
            if distance is None:
                self.results_area.insert(END, "Can walk indefinitely\n")
            else:
                self.results_area.insert(END, f"{distance}\n")
    def reset_data(self):  # Reset function to clear inputs and outputs
        self.text_area.delete("1.0", END)
        self.results_area.delete("1.0", END)
if __name__ == "__main__":
    root = Tk()
    app = RoadworkApp(root)
    root.mainloop()