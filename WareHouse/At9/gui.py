import tkinter as tk
from utils import validate_input, process_data
from database import Database
class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Song Phrase Checker")
        self.label = tk.Label(self.root, text="Enter the sequence of non-negative integers:")
        self.label.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.button = tk.Button(self.root, text="Check", command=self.check_phrase)
        self.button.pack()
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
        self.db = Database("data.db")
    def check_phrase(self):
        input_data = self.entry.get()
        if validate_input(input_data):
            data = list(map(int, input_data.split()))
            processed_data = process_data(data)
            self.db.insert_data(processed_data)
            retrieved_data = self.db.get_data()
            self.result_label.config(text=f"Processed Data: {processed_data}\nRetrieved Data: {retrieved_data}")
        else:
            self.result_label.config(text="Invalid input!")
    def __del__(self):
        self.db.close()