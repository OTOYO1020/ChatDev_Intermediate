'''
App class to create the GUI for the graph application.
'''
from tkinter import Frame, Label, Entry, Button, Text, Scrollbar, END
from graph import Graph
class App:
    def __init__(self, master):
        self.master = master
        master.title("Graph MST Application")
        self.graph_frame = Frame(master)
        self.graph_frame.pack()
        Label(self.graph_frame, text="Enter number of vertices:").grid(row=0, column=0)
        self.vertices_entry = Entry(self.graph_frame)
        self.vertices_entry.grid(row=0, column=1)
        Label(self.graph_frame, text="Enter number of edges:").grid(row=1, column=0)
        self.edges_entry = Entry(self.graph_frame)
        self.edges_entry.grid(row=1, column=1)
        Label(self.graph_frame, text="Enter edges (a, b, weight):").grid(row=2, column=0)
        self.edges_text = Text(self.graph_frame, height=10, width=30)
        self.edges_text.grid(row=3, columnspan=2)
        self.submit_graph_button = Button(self.graph_frame, text="Submit Graph", command=self.submit_graph)
        self.submit_graph_button.grid(row=4, columnspan=2)
        Label(self.graph_frame, text="Enter queries (u, v, w):").grid(row=5, column=0)
        self.queries_text = Text(self.graph_frame, height=10, width=30)
        self.queries_text.grid(row=6, columnspan=2)
        self.submit_query_button = Button(self.graph_frame, text="Submit Queries", command=self.submit_query)
        self.submit_query_button.grid(row=7, columnspan=2)
        self.result_text = Text(self.graph_frame, height=10, width=30)
        self.result_text.grid(row=8, columnspan=2)
        self.scrollbar = Scrollbar(self.graph_frame, command=self.result_text.yview)
        self.result_text['yscrollcommand'] = self.scrollbar.set
        self.scrollbar.grid(row=8, column=2, sticky='ns')
        self.graph = None
    def submit_graph(self):
        try:
            vertices = int(self.vertices_entry.get())
            edges = int(self.edges_entry.get())
        except ValueError:
            print("Invalid input format for number of vertices and edges. Expected integers.")
            return
        # Input validation
        if vertices <= 0 or edges < 0:
            print("Number of vertices must be positive and number of edges cannot be negative.")
            return
        # Edge count validation
        if edges < vertices - 1:
            print("Not enough edges to form a valid MST. At least N-1 edges are required.")
            return
        self.graph = Graph(vertices)
        edge_data = self.edges_text.get("1.0", END).strip().splitlines()  # Read edges from the dedicated area
        for line in edge_data:
            try:
                a, b, weight = map(int, line.split())
                if 1 <= a <= vertices and 1 <= b <= vertices:
                    self.graph.add_edge(a, b, weight)  # Adjusted for 1-based index
                else:
                    print(f"Invalid edge ({a}, {b}) - vertices must be between 1 and {vertices}.")
            except ValueError:
                print(f"Invalid input format for edge. Expected format: a b weight.")
        mst_valid, _ = self.graph.find_mst()  # Compute MST after adding edges
        if not mst_valid:  # Exit if the MST cannot be formed
            return
    def submit_query(self):
        if not self.graph.mst_edges:  # Check if MST is valid before processing queries
            self.result_text.delete("1.0", END)
            self.result_text.insert(END, "MST is invalid. Cannot process queries.\n")
            return
        queries = self.queries_text.get("1.0", END).strip().splitlines()
        results = []
        for line in queries:
            try:
                u, v, w = map(int, line.split())
                if 1 <= u <= self.graph.V and 1 <= v <= self.graph.V:
                    edge = (u, v, w)
                    if self.graph.is_edge_in_mst(edge, self.graph.mst_edges):  # Check if edge is in MST
                        results.append("Yes")
                    else:
                        results.append("No")
                else:
                    results.append(f"Invalid query ({u}, {v}) - vertices must be between 1 and {self.graph.V}.")
            except ValueError:
                results.append(f"Invalid input format for query. Expected format: u v w.")
        self.display_result(results)
    def display_result(self, results):
        self.result_text.delete("1.0", END)
        for result in results:
            self.result_text.insert(END, result + "\n")