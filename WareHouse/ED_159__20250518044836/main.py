'''
Main entry point for the Chocolate Cutting application.
'''
import json
from chocolate_cutting import min_cuts
import tkinter as tk
from tkinter import messagebox
class ChocolateCuttingApp:
    def __init__(self, master):
        self.master = master
        master.title("Chocolate Cutting Calculator")
        self.label_h = tk.Label(master, text="Height (H):")
        self.label_h.pack()
        self.entry_h = tk.Entry(master)
        self.entry_h.pack()
        self.label_w = tk.Label(master, text="Width (W):")
        self.label_w.pack()
        self.entry_w = tk.Entry(master)
        self.entry_w.pack()
        self.label_k = tk.Label(master, text="Max White Squares (K):")
        self.label_k.pack()
        self.entry_k = tk.Entry(master)
        self.entry_k.pack()
        self.label_s = tk.Label(master, text="Chocolate Bar (2D List):")
        self.label_s.pack()
        self.text_s = tk.Text(master, height=10, width=30)
        self.text_s.pack()
        self.calculate_button = tk.Button(master, text="Calculate Cuts", command=self.calculate_cuts)
        self.calculate_button.pack()
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
    def calculate_cuts(self):
        try:
            H = int(self.entry_h.get())
            W = int(self.entry_w.get())
            K = int(self.entry_k.get())
            S = json.loads(self.text_s.get("1.0", tk.END).strip())  # Expecting a list of lists
            if not (isinstance(S, list) and all(isinstance(row, list) for row in S)):
                raise ValueError("S must be a 2D list.")
            min_cuts_needed = min_cuts(H, W, K, S)
            self.display_result(min_cuts_needed)
        except Exception as e:
            messagebox.showerror("Input Error", str(e))
    def display_result(self, result):
        self.result_label.config(text=f"Minimum Cuts Required: {result}")
if __name__ == "__main__":
    root = tk.Tk()
    app = ChocolateCuttingApp(root)
    root.mainloop()