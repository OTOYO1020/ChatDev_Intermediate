'''
Main application file for finding the smallest integer X that satisfies the given conditions.
'''
import tkinter as tk
from computation import Computation
class App:
    '''
    Main application class that creates the GUI for user interaction.
    '''
    def __init__(self, master):
        self.master = master
        master.title("Find Smallest Integer X")
        self.label = tk.Label(master, text="Enter an integer N:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.find_button = tk.Button(master, text="Find X", command=self.find_smallest_x)
        self.find_button.pack()
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
    def find_smallest_x(self):
        '''
        Trigger the computation to find the smallest X based on user input.
        '''
        try:
            n = int(self.entry.get())
            computation = Computation()
            result = computation.find_x(n)
            self.result_label.config(text=f"The smallest X is: {result}")
        except ValueError:
            self.result_label.config(text="Please enter a valid integer.")
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()