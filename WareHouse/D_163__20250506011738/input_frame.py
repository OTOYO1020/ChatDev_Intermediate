'''
Input frame for entering values of N and K.
'''
from tkinter import Frame, Label, Entry
class InputFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label_n = Label(self, text="Enter N:")
        self.label_n.pack()
        self.entry_n = Entry(self)
        self.entry_n.pack()
        self.label_k = Label(self, text="Enter K:")
        self.label_k.pack()
        self.entry_k = Entry(self)
        self.entry_k.pack()
    def get_values(self):
        try:
            N = int(self.entry_n.get())
            K = int(self.entry_k.get())
            return N, K
        except ValueError:
            # Instead of printing, you could set a label in the GUI to show the error
            error_label = Label(self, text="Please enter valid integers for N and K.", fg="red")
            error_label.pack()
            return None, None  # Return None values to indicate an error