'''
Handles user input for the application.
'''
class InputHandler:
    def __init__(self):
        self.bags = []
        self.target_string = ""
        self.get_user_input()
    def get_user_input(self):
        num_bags = int(input("Enter the number of bags: "))
        for i in range(num_bags):
            bag_contents = input(f"Enter contents of bag {i + 1} (comma-separated): ")
            self.bags.append(bag_contents.split(","))
        self.target_string = input("Enter the target string: ")
    def get_input(self):
        return self.bags, self.target_string