'''
Contains the GUI class for the point transformation application.
'''
import tkinter as tk
from tkinter import messagebox
from transformations import transform_and_compare
class MainApp:
    '''
    Main application class for the GUI.
    '''
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Point Transformation Application")
        self.create_widgets()
    def create_widgets(self):
        '''
        Creates the GUI widgets.
        '''
        self.label_s = tk.Label(self.root, text="Enter points for set S (format: x1,y1 x2,y2 ...):")
        self.label_s.pack()
        self.entry_s = tk.Entry(self.root)
        self.entry_s.pack()
        self.label_t = tk.Label(self.root, text="Enter points for set T (format: x1,y1 x2,y2 ...):")
        self.label_t.pack()
        self.entry_t = tk.Entry(self.root)
        self.entry_t.pack()
        self.button = tk.Button(self.root, text="Transform and Compare", command=self.compare_sets)
        self.button.pack()
    def compare_sets(self):
        '''
        Handles the comparison of sets S and T.
        '''
        try:
            S = [tuple(map(float, point.split(','))) for point in self.entry_s.get().split()]
            T = [tuple(map(float, point.split(','))) for point in self.entry_t.get().split()]
            # Validate the input format
            if not all(len(point) == 2 for point in S) or not all(len(point) == 2 for point in T):
                raise ValueError("Each point must have exactly two coordinates.")
            result = transform_and_compare(S, T)
            self.display_result(result)
        except Exception as e:
            messagebox.showerror("Input Error", str(e))
    def display_result(self, result):
        '''
        Displays the result of the transformation comparison.
        '''
        if result:
            messagebox.showinfo("Result", "YES, S can be transformed to match T.")
        else:
            messagebox.showinfo("Result", "NO, S cannot be transformed to match T.")
    def run(self):
        '''
        Runs the main loop of the application.
        '''
        self.root.mainloop()