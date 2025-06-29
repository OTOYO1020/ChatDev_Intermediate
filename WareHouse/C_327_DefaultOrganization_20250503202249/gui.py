'''
Contains the GUI components for the Sudoku validation application.
'''
import tkinter as tk
from tkinter import messagebox
from validator import is_valid_sudoku
class SudokuApp:
    def __init__(self, master):
        """
        Initialize the Sudoku application GUI.
        """
        self.master = master
        self.master.title("Sudoku Validator")
        self.grid_entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_validate_button()
    def create_grid(self):
        """
        Create the 9x9 grid of entry fields.
        """
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.master, width=2, font=('Arial', 18), justify='center')
                entry.grid(row=i, column=j, padx=5, pady=5)
                self.grid_entries[i][j] = entry
    def create_validate_button(self):
        """
        Create the validate button.
        """
        validate_button = tk.Button(self.master, text="Validate", command=self.validate_grid)
        validate_button.grid(row=10, columnspan=9)
    def validate_grid(self):
        """
        Validate the Sudoku grid and display the result.
        """
        A = []
        for i in range(9):
            row = []
            for j in range(9):
                value = self.grid_entries[i][j].get()
                if value == "":  # Check for empty entries
                    messagebox.showerror("Input Error", "Please fill all cells with integers between 1 and 9.")
                    return
                try:
                    value = int(value)
                    if value < 1 or value > 9:
                        raise ValueError
                    row.append(value)
                except ValueError:
                    messagebox.showerror("Input Error", "Please enter integers between 1 and 9.")
                    return
            A.append(row)
        if len(A) != 9 or any(len(row) != 9 for row in A):
            messagebox.showerror("Input Error", "The grid must be a complete 9x9 grid.")
            return
        # Validate the entire grid
        if is_valid_sudoku(A):
            self.display_result("Yes")
        else:
            self.display_result("No")
    def display_result(self, result):
        """
        Display the validation result to the user.
        """
        messagebox.showinfo("Validation Result", f"The Sudoku grid is: {result}")