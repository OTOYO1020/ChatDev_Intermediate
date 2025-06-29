'''
Displays the results to the user.
'''
class OutputHandler:
    def __init__(self, app):
        self.app = app
    def display_result(self, valid_combinations):
        print(f"Valid combinations: {valid_combinations}")