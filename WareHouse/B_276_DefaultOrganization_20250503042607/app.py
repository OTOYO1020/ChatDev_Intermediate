'''
Module to define the App class for the GUI of the City Connections application.
'''
import tkinter as tk
from tkinter import messagebox
from city_graph import CityGraph
class App:
    def __init__(self, master):
        self.master = master
        master.title("City Connections")
        self.label = tk.Label(master, text="Enter number of cities:")
        self.label.pack()
        self.city_entry = tk.Entry(master)
        self.city_entry.pack()
        self.city_entry.insert(0, "Number of Cities")
        self.label_roads = tk.Label(master, text="Enter roads (one per line, format: A B):")
        self.label_roads.pack()
        self.road_entry = tk.Text(master, height=10, width=30)  # Changed to Text widget
        self.road_entry.pack()
        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()
        self.results_text = tk.Text(master)
        self.results_text.pack()
    def submit(self):
        try:
            num_cities = int(self.city_entry.get())
            roads_input = self.road_entry.get("1.0", tk.END).strip().splitlines()  # Get text from Text widget
            # Validate num_cities to ensure it is a positive integer
            if num_cities <= 0:
                messagebox.showerror("Input Error", "Number of cities must be a positive integer.")
                return
            graph = CityGraph(num_cities)
            for road in roads_input:
                if road:
                    city_a, city_b = map(int, road.split())
                    try:
                        graph.add_road(city_a, city_b)
                    except ValueError as e:
                        messagebox.showerror("Input Error", str(e))  # Show error for invalid city indices
                        return
            results = graph.get_connections()
            self.display_results(results)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers for cities and roads.")
    def display_results(self, results):
        self.results_text.delete(1.0, tk.END)  # Clear previous results
        for result in results:
            self.results_text.insert(tk.END, result + "\n")