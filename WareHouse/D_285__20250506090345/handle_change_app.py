'''
Module to handle user input and output for the handle change application.
'''
from user_handle_manager import UserHandleManager
class HandleChangeApp:
    def __init__(self):
        self.manager = UserHandleManager()
    def run(self):
        N = int(input("Enter the number of users: "))
        for _ in range(N):
            current_handle = input("Enter current handle: ")
            desired_handle = input("Enter desired handle: ")
            self.manager.add_user(current_handle, desired_handle)
        result = self.manager.process_handles()
        self.display_result(result)
    def display_result(self, result):
        if isinstance(result, str):
            print(result)
        else:
            change_order_str = "\n".join([f"{current} -> {desired}" for current, desired in result])
            print(f"Change Order:\n{change_order_str}")