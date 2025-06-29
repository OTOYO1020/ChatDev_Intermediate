'''
Manages the output display of results to the user.
'''
class OutputDisplay:
    def show_result(self, valid_lines):
        if valid_lines == "Infinity":
            print("Infinity")
        elif valid_lines > 0:
            print(f"Number of valid lines: {valid_lines}")
        else:
            print("No valid lines found.")