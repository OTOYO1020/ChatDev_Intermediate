'''
Main application file for the Color Grid application.
'''
from tkinter import Tk, Label, Entry, Button, Text, messagebox
from color_grid import count_colors
class ColorGridApp:
    '''
    Main application class for the Color Grid application.
    '''
    def __init__(self, master):
        '''
        Initializes the GUI components.
        '''
        self.master = master
        master.title("Color Grid Application")
        self.label = Label(master, text="Enter H, W, M (comma-separated):")
        self.label.pack()
        self.entry = Entry(master)
        self.entry.pack()
        self.instructions = Label(master, text="Enter operations as 'T A X' (one per line):")
        self.instructions.pack()
        self.text_area = Text(master, height=10, width=50)
        self.text_area.pack()
        self.run_button = Button(master, text="Run", command=self.run_operations)
        self.run_button.pack()
    def run_operations(self):
        '''
        Processes the input operations and updates the grid.
        '''
        try:
            input_data = self.entry.get().strip().split(',')
            H, W, M = map(int, input_data)
            operations = [tuple(map(int, op.split())) for op in self.text_area.get("1.0", "end-1c").strip().split('\n')]
            # Validate the number of operations
            if len(operations) != M:
                raise ValueError(f"Expected {M} operations, but got {len(operations)}.")
            # Validate each operation to ensure they are well-formed
            for op in operations:
                if len(op) != 3:
                    raise ValueError(f"Each operation must contain 3 values, but got {len(op)}.")
                T_i, A_i, X_i = op
                if T_i not in (1, 2):
                    raise ValueError(f"Invalid operation type {T_i}. Must be 1 or 2.")
                if (T_i == 1 and not (1 <= A_i <= H)) or (T_i == 2 and not (1 <= A_i <= W)):
                    raise ValueError(f"Index {A_i} is out of bounds for operation type {T_i}.")
            color_counts = count_colors(H, W, M, operations)
            self.display_results(color_counts)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def display_results(self, color_counts):
        '''
        Displays the color counts in a new window.
        '''
        result_window = Tk()
        result_window.title("Color Counts")
        result_text = "\n".join(f"Color {color}: {count}" for color, count in sorted(color_counts.items()))
        Label(result_window, text=result_text).pack()
        result_window.mainloop()
if __name__ == "__main__":
    root = Tk()
    app = ColorGridApp(root)
    root.mainloop()