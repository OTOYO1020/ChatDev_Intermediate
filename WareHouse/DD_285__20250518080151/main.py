'''
Main entry point of the Handle Change Application.
'''
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from handle_manager import HandleManager
from input_validator import InputValidator  # Import the InputValidator
class HandleChangeApp:
    def __init__(self, master):
        self.master = master
        master.title("Handle Change Application")
        self.label_n = Label(master, text="Number of Users (N):")
        self.label_n.pack()
        self.n_var = StringVar()
        self.entry_n = Entry(master, textvariable=self.n_var)
        self.entry_n.pack()
        self.label_s = Label(master, text="Current Handles (comma-separated):")
        self.label_s.pack()
        self.s_var = StringVar()
        self.entry_s = Entry(master, textvariable=self.s_var)
        self.entry_s.pack()
        self.label_t = Label(master, text="Desired Handles (comma-separated):")
        self.label_t.pack()
        self.t_var = StringVar()
        self.entry_t = Entry(master, textvariable=self.t_var)
        self.entry_t.pack()
        self.submit_button = Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()
    def submit(self):
        try:
            N = int(self.n_var.get())
            S = self.s_var.get().split(',')
            T = self.t_var.get().split(',')
            # Validate input before processing
            if not InputValidator.validate_input(N, S, T):
                messagebox.showerror("Error", "Invalid input. Please check the number of users and handles.")
                return
            manager = HandleManager()
            result = manager.canChangeHandles(N, S, T)
            messagebox.showinfo("Result", str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))
if __name__ == "__main__":
    root = Tk()
    app = HandleChangeApp(root)
    root.mainloop()