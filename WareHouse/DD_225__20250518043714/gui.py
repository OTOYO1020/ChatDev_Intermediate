'''
Module to create the GUI for the toy train application.
'''
import tkinter as tk
from tkinter import messagebox
from train_network import TrainNetwork
class TrainApp:
    def __init__(self, N=5):  # Allow N to be passed in
        self.network = TrainNetwork(N)  # Initialize with N
        self.window = tk.Tk()
        self.window.title("Toy Train Network")
        self.create_widgets()
    def create_widgets(self):
        self.connect_frame = tk.Frame(self.window)
        self.connect_frame.pack()
        self.label_connect = tk.Label(self.connect_frame, text="Connect Cars:")
        self.label_connect.grid(row=0, column=0)
        self.entry_x = tk.Entry(self.connect_frame)
        self.entry_x.grid(row=0, column=1)
        self.entry_y = tk.Entry(self.connect_frame)
        self.entry_y.grid(row=0, column=2)
        self.button_connect = tk.Button(self.connect_frame, text="Connect", command=self.connect_cars)
        self.button_connect.grid(row=0, column=3)
        self.disconnect_frame = tk.Frame(self.window)
        self.disconnect_frame.pack()
        self.label_disconnect = tk.Label(self.disconnect_frame, text="Disconnect Cars:")
        self.label_disconnect.grid(row=0, column=0)
        self.entry_x_disconnect = tk.Entry(self.disconnect_frame)
        self.entry_x_disconnect.grid(row=0, column=1)
        self.entry_y_disconnect = tk.Entry(self.disconnect_frame)
        self.entry_y_disconnect.grid(row=0, column=2)
        self.button_disconnect = tk.Button(self.disconnect_frame, text="Disconnect", command=self.disconnect_cars)
        self.button_disconnect.grid(row=0, column=3)
        self.retrieve_frame = tk.Frame(self.window)
        self.retrieve_frame.pack()
        self.label_retrieve = tk.Label(self.retrieve_frame, text="Retrieve Component for Car:")
        self.label_retrieve.grid(row=0, column=0)
        self.entry_retrieve = tk.Entry(self.retrieve_frame)
        self.entry_retrieve.grid(row=0, column=1)
        self.button_retrieve = tk.Button(self.retrieve_frame, text="Retrieve", command=self.retrieve_connected_component)
        self.button_retrieve.grid(row=0, column=2)
    def connect_cars(self):
        try:
            x = int(self.entry_x.get())
            y = int(self.entry_y.get())
            if not (1 <= x <= 5) or not (1 <= y <= 5):  # Assuming N = 5
                raise ValueError("Car numbers must be between 1 and 5.")
            self.network.add_connection(x, y)
            messagebox.showinfo("Success", f"Connected Car {x} to Car {y}")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
    def disconnect_cars(self):
        try:
            x = int(self.entry_x_disconnect.get())
            y = int(self.entry_y_disconnect.get())
            if not (1 <= x <= 5) or not (1 <= y <= 5):  # Assuming N = 5
                raise ValueError("Car numbers must be between 1 and 5.")
            try:
                self.network.remove_connection(x, y)  # No exception raised
                messagebox.showinfo("Success", f"Disconnected Car {x} from Car {y}")
            except ValueError as e:
                messagebox.showerror("Disconnection Error", str(e))
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
    def retrieve_connected_component(self):
        try:
            x = int(self.entry_retrieve.get())
            if not (1 <= x <= 5):  # Assuming N = 5
                raise ValueError("Car number must be between 1 and 5.")
            component = self.network.get_connected_component(x)
            messagebox.showinfo("Connected Component", f"Cars connected to {x}: {' '.join(map(str, component))}")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
    def run(self):
        self.window.mainloop()