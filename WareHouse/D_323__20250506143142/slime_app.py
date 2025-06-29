'''
This module defines the SlimeApp class, which handles the command-line interface for the slime synthesis application.
'''
from slime_manager import SlimeManager
class SlimeApp:
    def __init__(self):
        self.manager = SlimeManager()
    def run(self):
        '''
        Runs the application, prompting the user for input and managing the slime synthesis process.
        '''
        while True:
            try:
                N = int(input("Enter the number of different slime sizes (positive integer): "))
                if N < 1:
                    raise ValueError("The number of sizes must be at least 1.")
                break  # Exit the loop if input is valid
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
        for _ in range(N):
            while True:
                try:
                    size, count = map(int, input("Please enter the slime size (>= 1) and count (>= 0) separated by a space: ").split())
                    if size < 1 or count < 0:
                        raise ValueError("Size must be >= 1 and count must be >= 0.")
                    self.manager.add_slime(size, count)
                    break  # Exit the loop if input is valid
                except ValueError as e:
                    print(f"Invalid input: {e}. Please try again.")
        self.manager.synthesize_slimes()
        final_count = self.manager.get_final_slime_count()
        print(f"Final number of slimes: {final_count}")