'''
Main application file for the Typing Time Calculator.
'''
from tkinter import Tk, Label, Entry, Button, StringVar
from typing_logic import min_time_to_type
class TypingApp:
    def __init__(self, master):
        self.master = master
        master.title("Typing Time Calculator")
        self.label = Label(master, text="Enter string (S):")
        self.label.pack()
        self.input_string = StringVar()
        self.entry = Entry(master, textvariable=self.input_string)
        self.entry.pack()
        self.label_x = Label(master, text="Time to press 'A' or 'a' (X):")
        self.label_x.pack()
        self.input_x = StringVar()
        self.entry_x = Entry(master, textvariable=self.input_x)
        self.entry_x.pack()
        self.label_y = Label(master, text="Time to press Shift + 'A' or 'a' (Y):")
        self.label_y.pack()
        self.input_y = StringVar()
        self.entry_y = Entry(master, textvariable=self.input_y)
        self.entry_y.pack()
        self.label_z = Label(master, text="Time to toggle Caps Lock (Z):")
        self.label_z.pack()
        self.input_z = StringVar()
        self.entry_z = Entry(master, textvariable=self.input_z)
        self.entry_z.pack()
        self.calculate_button = Button(master, text="Calculate Time", command=self.calculate_time)
        self.calculate_button.pack()
        self.result_label = Label(master, text="")
        self.result_label.pack()
    def calculate_time(self):
        S = self.input_string.get()
        X = int(self.input_x.get())
        Y = int(self.input_y.get())
        Z = int(self.input_z.get())
        total_time = min_time_to_type(S, X, Y, Z)
        self.result_label.config(text=f"Total Time: {total_time}")
if __name__ == "__main__":
    root = Tk()
    app = TypingApp(root)
    root.mainloop()