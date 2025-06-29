'''
Main application file for the Median Calculator.
'''
from tkinter import Tk, Label, Entry, Button, Text, END
from median_calculator import count_distinct_median
class MedianCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Median Calculator")
        self.label = Label(master, text="Enter number of pairs (N):")
        self.label.pack()
        self.n_entry = Entry(master)
        self.n_entry.pack()
        self.text_area = Text(master, height=10, width=30)
        self.text_area.pack()
        self.calculate_button = Button(master, text="Calculate Median", command=self.calculate_median)
        self.calculate_button.pack()
        self.result_label = Label(master, text="")
        self.result_label.pack()
    def calculate_median(self):
        try:
            # Validate N input
            N = int(self.n_entry.get())
            if N <= 0:
                self.result_label.config(text="Error: N must be a positive integer.")
                return
            input_data = self.text_area.get("1.0", END).strip().splitlines()
            # Validate the number of pairs
            if len(input_data) != N:
                self.result_label.config(text=f"Error: Expected {N} pairs, but got {len(input_data)}.")
                return
            A = []
            B = []
            for line in input_data:
                parts = line.split()
                # Ensure each line contains exactly two integers
                if len(parts) != 2:
                    self.result_label.config(text="Error: Each line must contain exactly two integers (A_i B_i).")
                    return
                try:
                    a, b = map(int, parts)
                    # Validate that A[i] <= B[i]
                    if a > b:
                        self.result_label.config(text="Error: Lower bound must not be greater than upper bound (A_i <= B_i).")
                        return
                    A.append(a)
                    B.append(b)
                except ValueError:
                    self.result_label.config(text="Error: Please enter valid integers for A_i and B_i.")
                    return
            median_count = count_distinct_median(N, A, B)
            self.result_label.config(text=f"Distinct Median Values: {median_count}")
        except ValueError:
            self.result_label.config(text="Error: Please enter a valid integer for N.")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")
if __name__ == "__main__":
    root = Tk()
    app = MedianCalculatorApp(root)
    root.mainloop()