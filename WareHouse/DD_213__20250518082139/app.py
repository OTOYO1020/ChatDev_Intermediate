'''
Module to create the GUI for the city traversal application.
'''
from tkinter import Frame, Label, Button, Entry, Text, Scrollbar, END
from city_graph import CityGraph
from typing import List, Tuple
import ast
import re
class App:
    def __init__(self, master):
        self.master = master
        master.title("City Traversal Application")
        self.label = Label(master, text="Enter number of cities and roads (e.g., 5, [(1, 2), (2, 3), (3, 4), (4, 5)])")
        self.label.pack()
        self.entry = Entry(master, width=50)
        self.entry.pack()
        self.run_button = Button(master, text="Run Traversal", command=self.run_traversal)
        self.run_button.pack()
        self.result_text = Text(master, height=10, width=50)
        self.result_text.pack()
        self.scrollbar = Scrollbar(master, command=self.result_text.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.result_text['yscrollcommand'] = self.scrollbar.set
    def run_traversal(self):
        input_data = self.entry.get()
        try:
            if not input_data.strip():
                raise ValueError("Input cannot be empty.")
            # Use regex to extract N and roads with improved handling for spaces
            match = re.match(r'(\d+)\s*,\s*\[(.*)\]', input_data.strip())
            if not match:
                raise ValueError("Input format is incorrect. Expected format: 'N, [(a, b), ...]'")
            N = int(match.group(1))
            roads_str = match.group(2)
            if not roads_str:
                roads = []
            else:
                roads = ast.literal_eval(f"[{roads_str}]")
            # Validate roads format
            if not all(isinstance(road, tuple) and len(road) == 2 and all(isinstance(x, int) for x in road) for road in roads):
                raise ValueError("Roads must be a list of tuples (a, b) where a and b are integers.")
            graph = CityGraph(N, roads)
            result = graph.find_visited_cities()
            self.display_result(result)
        except Exception as e:
            self.display_result(f"Error: {str(e)}")
    def display_result(self, result):
        self.result_text.delete(1.0, END)  # Clear previous results
        self.result_text.insert(END, str(result))  # Display new result