'''
Main application file for the Good Sequences Calculator.
'''
from tkinter import Tk, Label, Entry, Button, Text, END  # Added missing imports
from typing import List, Tuple
from good_sequences import count_good_sequences
import ast  # Importing ast for safe evaluation of input
class GoodSequenceApp:
    def __init__(self, master):
        self.master = master
        master.title("Good Sequences Calculator")
        self.label_m = Label(master, text="Enter maximum integer (M):")
        self.label_m.pack()
        self.entry_m = Entry(master)
        self.entry_m.pack()
        self.label_pairs = Label(master, text="Enter pairs (e.g., (1, 2), (3, 4)):")
        self.label_pairs.pack()
        self.entry_pairs = Entry(master)
        self.entry_pairs.pack()
        self.calculate_button = Button(master, text="Calculate", command=self.calculate_good_sequences)
        self.calculate_button.pack()
        self.result_text = Text(master, height=10, width=50)
        self.result_text.pack()
    def calculate_good_sequences(self):
        '''
        Calculate good sequences based on user input and display the result.
        '''
        try:
            M = int(self.entry_m.get())
            pairs_input = self.entry_pairs.get()
            pairs = ast.literal_eval(pairs_input)  # Use ast.literal_eval for safety
            result = count_good_sequences(M, pairs)
            self.result_text.delete(1.0, END)
            self.result_text.insert(END, str(result))
        except Exception as e:
            self.result_text.delete(1.0, END)
            self.result_text.insert(END, f"Error: {str(e)}")
if __name__ == "__main__":
    root = Tk()
    app = GoodSequenceApp(root)
    root.mainloop()