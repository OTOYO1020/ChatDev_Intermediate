'''
This file contains the controller implementation.
'''
from logic import Logic
from gui import GUI
class Controller:
    def __init__(self, root):
        self.root = root
        self.gui = GUI(self.root)
        self.logic = Logic()
        self.gui.logic = self.logic
        self.gui.register_callback(self.perform_task)
    def perform_task(self):
        A = [int(x) for x in self.gui.entry_A.get().split()]
        B = [int(x) for x in self.gui.entry_B.get().split()]
        M = int(self.gui.entry_M.get())
        count, A, B, C = self.logic.perform_task(A, B, M)
        print("Number of integers satisfying the condition:", count)
        print("Updated sequence A:", A)
        print("Updated sequence B:", B)
        print("Updated sequence C:", C)