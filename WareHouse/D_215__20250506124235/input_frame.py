'''
Module for creating the input frame for user inputs.
'''
from tkinter import Frame, Label, Entry, Button, StringVar
class InputFrame(Frame):
    def __init__(self, master, result_frame):
        super().__init__(master)
        self.result_frame = result_frame
        self.label_n = Label(self, text="Enter N:")
        self.label_n.grid(row=0, column=0)
        self.n_value = StringVar()
        self.entry_n = Entry(self, textvariable=self.n_value)
        self.entry_n.grid(row=0, column=1)
        self.label_m = Label(self, text="Enter M:")
        self.label_m.grid(row=1, column=0)
        self.m_value = StringVar()
        self.entry_m = Entry(self, textvariable=self.m_value)
        self.entry_m.grid(row=1, column=1)
        self.label_a = Label(self, text="Enter A (comma-separated positive integers):")  # Clarified input format
        self.label_a.grid(row=2, column=0)
        self.a_values = StringVar()
        self.entry_a = Entry(self, textvariable=self.a_values)
        self.entry_a.grid(row=2, column=1)
        self.calculate_button = Button(self, text="Calculate Coprimes", command=self.calculate_callback)
        self.calculate_button.grid(row=3, columnspan=2)
    def calculate_callback(self):
        from main import calculate_coprimes  # Local import to avoid circular dependency
        try:
            N = int(self.n_value.get())
            M = int(self.m_value.get())
            if N <= 0 or M <= 0:
                raise ValueError("N and M must be positive integers.")
            # Validate A input
            A = [a.strip() for a in self.a_values.get().split(',')]
            if len(A) != N:
                raise ValueError(f"Expected {N} integers in A, but got {len(A)}.")
            # Check if all integers in A are positive and convert to integers
            A = [int(a) for a in A if a.isdigit() and int(a) > 0]
            if len(A) != N:
                raise ValueError(f"Expected {N} positive integers in A, but got {len(A)}.")
            results = calculate_coprimes(N, M, A)
            self.result_frame.display_results(results)
        except ValueError as ve:
            self.result_frame.display_results(f"Input Error: {ve}")  # Display error in GUI
        except Exception as e:
            self.result_frame.display_results(f"Error: {e}")  # Display error in GUI
    def get_inputs(self):
        return self.n_value.get(), self.m_value.get(), self.a_values.get()