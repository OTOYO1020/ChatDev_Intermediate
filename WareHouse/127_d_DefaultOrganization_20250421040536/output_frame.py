'''
Contains the OutputFrame class for displaying results.
'''
class OutputFrame:
    def __init__(self):
        self.result = None
    def display_result(self, result):
        self.result = result
        print(f"Maximum Sum: {self.result}")