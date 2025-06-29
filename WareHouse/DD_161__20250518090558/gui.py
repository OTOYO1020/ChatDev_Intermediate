'''
This module contains the GUI application for finding lunlun numbers.
'''
import tkinter as tk
from tkinter import messagebox
from lunlun import find_kth_lunlun_number
class LunlunApp:
    """
    A class to create the GUI for the lunlun number finder application.
    """
    def __init__(self, master):
        self.master = master
        master.title("Lunlun Number Finder")
        self.label = tk.Label(master, text="Enter K (1 ≤ K ≤ 100000):")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.find_button = tk.Button(master, text="Find K-th Lunlun Number", command=self.find_lunlun)
        self.find_button.pack()
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
    def find_lunlun(self):
        """
        Handle the button click event to find the K-th lunlun number.
        """
        try:
            K = int(self.entry.get())
            if 1 <= K <= 100000:
                result = find_kth_lunlun_number(K)
                self.result_label.config(text=f"The {K}-th lunlun number is: {result}")
            else:
                messagebox.showerror("Input Error", "K must be between 1 and 100000.")
        except ValueError as e:
            messagebox.showerror("Input Error", f"Please enter a valid integer. {e}")