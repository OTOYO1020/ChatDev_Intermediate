'''
This module creates the GUI for the cookie management application.
'''
from tkinter import Frame, Label, Entry, Button, Text, messagebox
from cookie_manager import CookieManager
class App:
    def __init__(self, master):
        self.master = master
        self.create_widgets()
    def create_widgets(self):
        self.label_height = Label(self.master, text="Height (H):")
        self.label_height.pack()
        self.entry_height = Entry(self.master)
        self.entry_height.pack()
        self.label_width = Label(self.master, text="Width (W):")
        self.label_width.pack()
        self.entry_width = Entry(self.master)
        self.entry_width.pack()
        self.label_cookies = Label(self.master, text="Enter cookie colors (one row per line):")
        self.label_cookies.pack()
        self.text_cookies = Text(self.master, height=10, width=30)
        self.text_cookies.pack()
        self.button_process = Button(self.master, text="Process Cookies", command=self.process_cookies)
        self.button_process.pack()
    def process_cookies(self):
        try:
            height = int(self.entry_height.get())
            width = int(self.entry_width.get())
            cookie_colors = self.text_cookies.get("1.0", "end-1c").strip().splitlines()
            if len(cookie_colors) != height or any(len(row) != width for row in cookie_colors):
                raise ValueError("Input dimensions do not match the specified height and width.")
            if any(not all(c.islower() and c.isalpha() for c in row) for row in cookie_colors):
                raise ValueError("All cookie colors must be lowercase English letters.")
            manager = CookieManager(height, width)
            manager.add_cookies(cookie_colors)
            while True:
                manager.mark_cookies()
                if any(any(row) for row in manager.marked):
                    manager.remove_marked_cookies()
                else:
                    break
            remaining_count = manager.count_remaining_cookies()
            messagebox.showinfo("Result", f"Remaining cookies: {remaining_count}")
        except Exception as e:
            messagebox.showerror("Error", str(e))