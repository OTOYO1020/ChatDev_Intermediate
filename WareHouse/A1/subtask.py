'''
This file contains the Subtask class.
'''
class Subtask:
    def __init__(self):
        self.task_description = ""
    def set_task_description(self, task_description):
        self.task_description = task_description
    def execute(self):
        if self.task_description == "Game Over":
            # Perform action for game over
            print("Game Over")
        else:
            # Perform default action
            print("Executing subtask with task description:", self.task_description)