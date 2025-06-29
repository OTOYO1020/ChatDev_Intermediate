'''
Module to define the GUI for the graph application using Tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from graph import Graph
class GraphApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Graph Application")
        self.graph = None  # Initialize graph as None
        self.create_widgets()
    def create_widgets(self):
        # Number of vertices input section
        self.vertex_frame = tk.Frame(self.root)
        self.vertex_frame.pack(pady=10)
        tk.Label(self.vertex_frame, text="Enter the number of vertices:").grid(row=0, column=0)
        self.num_vertices_entry = tk.Entry(self.vertex_frame)
        self.num_vertices_entry.grid(row=0, column=1)
        tk.Button(self.vertex_frame, text="Set Vertices", command=self.set_vertices).grid(row=0, column=2)
        # Add edge section
        self.add_edge_frame = tk.Frame(self.root)
        self.add_edge_frame.pack(pady=10)
        tk.Label(self.add_edge_frame, text="Add Edge (u, v):").grid(row=0, column=0)
        self.u_entry = tk.Entry(self.add_edge_frame)
        self.u_entry.grid(row=0, column=1)
        self.v_entry = tk.Entry(self.add_edge_frame)
        self.v_entry.grid(row=0, column=2)
        tk.Button(self.add_edge_frame, text="Add Edge", command=self.add_edge).grid(row=0, column=3)
        # Find k-th largest section
        self.find_kth_frame = tk.Frame(self.root)
        self.find_kth_frame.pack(pady=10)
        tk.Label(self.find_kth_frame, text="Find k-th Largest (v, k):").grid(row=0, column=0)
        self.v_k_entry = tk.Entry(self.find_kth_frame)
        self.v_k_entry.grid(row=0, column=1)
        self.k_entry = tk.Entry(self.find_kth_frame)
        self.k_entry.grid(row=0, column=2)
        tk.Button(self.find_kth_frame, text="Find", command=self.find_kth_largest).grid(row=0, column=3)
    def set_vertices(self):
        try:
            num_vertices = int(self.num_vertices_entry.get())
            self.graph = Graph(num_vertices)  # Initialize graph with user input
            messagebox.showinfo("Success", f"Graph initialized with {num_vertices} vertices.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for the number of vertices.")
    def add_edge(self):
        try:
            u = int(self.u_entry.get())
            v = int(self.v_entry.get())
            if self.graph is not None:
                if self.graph.add_edge(u, v):
                    messagebox.showinfo("Success", f"Edge added between {u} and {v}.")
                else:
                    messagebox.showerror("Error", f"Failed to add edge between {u} and {v}.")
            else:
                messagebox.showerror("Error", "Please set the number of vertices first.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for u and v.")
    def find_kth_largest(self):
        try:
            v = int(self.v_k_entry.get())
            k = int(self.k_entry.get())
            if self.graph is not None:
                result = self.graph.find_kth_largest(v, k)
                if result != -1:
                    messagebox.showinfo("Result", f"The {k}-th largest vertex connected to {v} is {result}.")
                else:
                    messagebox.showinfo("Result", f"There are not enough vertices connected to {v} or k is invalid.")
            else:
                messagebox.showerror("Error", "Please set the number of vertices first.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for v and k.")
    def run(self):
        self.root.mainloop()