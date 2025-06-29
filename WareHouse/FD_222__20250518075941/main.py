'''
Main entry point of the application.
'''
from tkinter import Tk, Label, Button, Text, Scrollbar, END
from graph import Graph
from utils import get_input_data, display_results
class App:
    def __init__(self, master):
        self.master = master
        master.title("Travel Cost Calculator")
        self.label = Label(master, text="Enter towns, roads, and sightseeing costs:")
        self.label.pack()
        self.text_input = Text(master, height=10, width=50)
        self.text_input.pack()
        self.calculate_button = Button(master, text="Calculate Travel Costs", command=self.calculate_costs)
        self.calculate_button.pack()
        self.results_text = Text(master, height=10, width=50)
        self.results_text.pack()
        self.scrollbar = Scrollbar(master, command=self.results_text.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.results_text.config(yscrollcommand=self.scrollbar.set)
    def calculate_costs(self):
        input_data = self.text_input.get("1.0", END).strip()
        try:
            towns, roads, sightseeing_costs = get_input_data(input_data)
            graph = Graph(towns, roads, sightseeing_costs)
            results = graph.max_travel_cost()
            display_results(self.results_text, results)
        except ValueError as e:
            self.results_text.delete("1.0", END)
            self.results_text.insert(END, f"Error: {str(e)}\n")
if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()