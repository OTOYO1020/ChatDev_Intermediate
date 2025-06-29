'''
InputFrame class to manage user input.
'''
from tkinter import Button, Entry, Frame, Label, StringVar, messagebox


class InputFrame(Frame):
    def __init__(self, master, run_algorithm):
        super().__init__(master)
        self.run_algorithm = run_algorithm
        self.n_var = StringVar()
        self.m_var = StringVar()
        self.constraints = []
        self.constraint_vars = []  # To keep track of constraint input fields
        Label(self, text="Enter N:").grid(row=0, column=0)
        Entry(self, textvariable=self.n_var).grid(row=0, column=1)
        Label(self, text="Enter M:").grid(row=1, column=0)
        Entry(self, textvariable=self.m_var).grid(row=1, column=1)
        self.run_button = Button(self, text="Run Algorithm", command=self.run_algorithm, state='disabled')
        self.run_button.grid(row=3, column=0, columnspan=2)
        Button(self, text="Add Constraint", command=self.add_constraint).grid(row=2, column=0, columnspan=2)
    def add_constraint(self):
        # Check if N and M are set before allowing constraints to be added
        if not self.n_var.get() or not self.m_var.get():
            messagebox.showerror("Input Error", "Error: Please enter valid values for N and M before adding constraints.")
            return
        # Create new input fields for X, Y, Z
        x_var = StringVar()
        y_var = StringVar()
        z_var = StringVar()
        self.constraint_vars.extend([x_var, y_var, z_var])  # Store the vars for later clearing
        # Create labels and entries for X, Y, Z
        row = len(self.constraints) + 4  # Adjust row based on existing constraints
        Label(self, text="Enter X:").grid(row=row, column=0)
        Entry(self, textvariable=x_var).grid(row=row, column=1)
        Label(self, text="Enter Y:").grid(row=row + 1, column=0)
        Entry(self, textvariable=y_var).grid(row=row + 1, column=1)
        Label(self, text="Enter Z:").grid(row=row + 2, column=0)
        Entry(self, textvariable=z_var).grid(row=row + 2, column=1)
        # Add button to save the constraint
        Button(self, text="Save Constraint", command=lambda: self.save_constraint(x_var, y_var, z_var)).grid(row=row + 3, column=0, columnspan=2)
    def save_constraint(self, x_var, y_var, z_var):
        try:
            # Convert inputs to integers
            x = int(x_var.get())
            y = int(y_var.get())
            z = int(z_var.get())

            x_var.set('')
            y_var.set('')
            z_var.set('')
            self.run_button.config(state='normal')  # Enable the run button after adding a constraint
        except ValueError:
            messagebox.showerror("Input Error", "Error: X, Y, and Z must be valid integers.")
    def get_input(self):
        try:
            n = int(self.n_var.get())
            m = int(self.m_var.get())
            if not self.constraints:  # Check if constraints are empty
                messagebox.showerror("Input Error", "Error: At least one constraint must be added.")
                return n, m, None  # Return None for constraints to indicate an error
            return n, m, self.constraints
        except ValueError:
            messagebox.showerror("Input Error", "Error: N and M must be valid integers.")
            return None, None, None  # Return None for all to indicate an error
    def reset_constraints(self):
        self.constraints = []  # Reset constraints before getting new input
        for var in self.constraint_vars:
            var.set('')  # Clear the input fields for constraints
        self.constraint_vars.clear()  # Clear the list of constraint variables
        self.run_button.config(state='disabled')  # Disable the run button