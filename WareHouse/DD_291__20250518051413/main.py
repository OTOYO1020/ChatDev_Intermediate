'''
Main entry point for the Card Flip application.
'''
from tkinter import Tk, Label, Entry, Button, StringVar
from card_flip import count_valid_flips
class CardFlipApp:
    def __init__(self, master):
        self.master = master
        master.title("Card Flip Counter")
        self.label = Label(master, text="Enter N (1-100); A (comma-separated); B (comma-separated):")
        self.label.pack()
        self.input_var = StringVar()
        self.input_entry = Entry(master, textvariable=self.input_var)
        self.input_entry.pack()
        self.result_var = StringVar()
        self.result_label = Label(master, textvariable=self.result_var)
        self.result_label.pack()
        self.calculate_button = Button(master, text="Calculate Valid Flips", command=self.count_flips)
        self.calculate_button.pack()
    def count_flips(self):
        try:
            input_data = self.input_var.get().strip()
            n_str, a_str, b_str = input_data.split(';')
            N = int(n_str)
            A = list(map(int, a_str.split(',')))
            B = list(map(int, b_str.split(',')))
            if N != len(A) or N != len(B):
                raise ValueError("Length of A and B must be equal to N.")
            if N < 1 or N > 100:  # Assuming N should be between 1 and 100
                raise ValueError("N must be between 1 and 100.")
            result = count_valid_flips(N, A, B)
            self.result_var.set(f"Valid Configurations: {result}")
        except Exception as e:
            self.result_var.set(f"Error: {str(e)}. Please use the format: N;A1,A2,...;B1,B2,...")
if __name__ == "__main__":
    root = Tk()
    app = CardFlipApp(root)
    root.mainloop()