'''
Handles user input for the number of cities and roads.
'''
import tkinter as tk
from tkinter import simpledialog, messagebox
class InputDialog:
    def __init__(self, master, callback):
        self.master = master
        self.callback = callback
        self.dialog = tk.Toplevel(master)
        self.dialog.title("Input Cities and Roads")
        self.num_cities_label = tk.Label(self.dialog, text="Number of Cities:")
        self.num_cities_label.pack()
        self.num_cities_entry = tk.Entry(self.dialog)
        self.num_cities_entry.pack()
        self.roads_label = tk.Label(self.dialog, text="Enter roads as 'A B' (one per line, empty line to finish):")
        self.roads_label.pack()
        self.roads_text = tk.Text(self.dialog, height=10, width=30)
        self.roads_text.pack()
        self.submit_button = tk.Button(self.dialog, text="Submit", command=self.submit)
        self.submit_button.pack()
    def submit(self):
        try:
            num_cities = int(self.num_cities_entry.get())
            if num_cities < 1:  # Validate number of cities
                raise ValueError("Number of cities must be at least 1.")
            # If there's only one city, no roads should be entered
            if num_cities == 1:
                self.callback(num_cities, [])
                self.dialog.destroy()
                return
            roads_input = self.roads_text.get("1.0", tk.END).strip().splitlines()
            roads = []
            for line in roads_input:
                if line.strip():  # Only process non-empty lines
                    parts = line.split()
                    if len(parts) != 2:  # Ensure there are exactly two parts
                        raise ValueError(f"Invalid road format: '{line}'. Each road must consist of two integers.")
                    city_a, city_b = map(int, parts)
                    roads.append((city_a, city_b))
            # Validate roads
            seen_roads = set()
            for city_a, city_b in roads:
                if city_a < 1 or city_a > num_cities or city_b < 1 or city_b > num_cities:
                    raise ValueError(f"Roads must connect cities between 1 and {num_cities}. Invalid road: {city_a} - {city_b}")
                if city_a == city_b:
                    raise ValueError(f"Self-loops are not allowed. Invalid road: {city_a} - {city_b}")
                if (city_a, city_b) in seen_roads or (city_b, city_a) in seen_roads:
                    raise ValueError(f"Duplicate roads are not allowed. Invalid road: {city_a} - {city_b}")
                seen_roads.add((city_a, city_b))
            # Ensure exactly N-1 roads are provided
            if num_cities > 1 and len(roads) != num_cities - 1:
                raise ValueError(f"Exactly {num_cities - 1} roads must be provided for {num_cities} cities.")
            self.callback(num_cities, roads)
            self.dialog.destroy()
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))