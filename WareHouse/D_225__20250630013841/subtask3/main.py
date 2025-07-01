'''
This file contains the TrainApp class which sets up the GUI for managing toy train cars.
'''
import tkinter as tk
from train import Train
class TrainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Toy Train Manager")
        self.train = Train()
        self.setup_ui()
    def setup_ui(self):
        self.input_frame = tk.Frame(self.master)
        self.input_frame.pack()
        self.query_label = tk.Label(self.input_frame, text="Enter Query:")
        self.query_label.pack(side=tk.LEFT)
        self.query_entry = tk.Entry(self.input_frame)
        self.query_entry.pack(side=tk.LEFT)
        self.submit_button = tk.Button(self.input_frame, text="Submit", command=self.process_query)
        self.submit_button.pack(side=tk.LEFT)
        self.output_frame = tk.Frame(self.master)
        self.output_frame.pack()
        self.output_label = tk.Label(self.output_frame, text="Output:")
        self.output_label.pack()
        self.output_text = tk.Text(self.output_frame, height=10, width=50)
        self.output_text.pack()
    def process_query(self):
        query = self.query_entry.get()
        self.query_entry.delete(0, tk.END)
        parts = query.split()
        if not parts:
            return
        query_type = int(parts[0])
        if query_type == 1:  # connect
            x, y = int(parts[1]), int(parts[2])
            self.train.connect(x, y)
            self.output_text.insert(tk.END, f"Connected {x} to {y}\n")
        elif query_type == 2:  # disconnect
            x, y = int(parts[1]), int(parts[2])
            self.train.disconnect(x, y)
            self.output_text.insert(tk.END, f"Disconnected {x} from {y}\n")
        elif query_type == 3:  # print connected component
            x = int(parts[1])
            component = self.train.print_connected_component(x)
            self.output_text.insert(tk.END, f"Connected component of {x}: {component}\n")
def main():
    root = tk.Tk()
    app = TrainApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()