'''
Module to define the App class for the GUI of the graph query application.
'''
import tkinter as tk
from tkinter import messagebox
from graph import Graph
from query_processor import QueryProcessor
class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Graph Query Application")
        self.graph = None  # Initialize without a graph
        self.query_processor = None  # Initialize without a query processor
        self.label = tk.Label(master, text="Enter number of vertices:")
        self.label.pack()
        self.vertex_entry = tk.Entry(master)
        self.vertex_entry.pack()
        self.query_text = tk.Text(master, height=10, width=50)
        self.query_text.pack()
        self.submit_button = tk.Button(master, text="Submit Queries", command=self.submit_query)
        self.submit_button.pack()
    def submit_query(self):
        try:
            vertices = int(self.vertex_entry.get())
            self.graph = Graph(vertices)  # Initialize with the correct number of vertices
            self.query_processor = QueryProcessor(self.graph)
            queries = self.query_text.get("1.0", tk.END).strip().splitlines()
            query_list = []
            for query in queries:
                parts = list(map(int, query.split()))
                if parts[0] == 1 and len(parts) == 3:
                    query_list.append((1, (parts[1], parts[2])))
                elif parts[0] == 2 and len(parts) == 3:
                    query_list.append((2, (parts[1], parts[2])))
                else:
                    messagebox.showerror("Error", "Invalid query format. Type 1 should have 3 integers and Type 2 should have 3 integers.")
                    return
            results = self.query_processor.process_queries(query_list)
            if not results:
                messagebox.showinfo("Results", "No results to display.")
            else:
                self.display_results(results)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def display_results(self, results):
        result_str = "\n".join(map(str, results))
        messagebox.showinfo("Results", result_str)