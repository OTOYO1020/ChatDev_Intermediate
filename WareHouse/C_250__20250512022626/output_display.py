'''
Handles the display of output for the Ball Swapper application.
'''
class OutputDisplay:
    def display_output(self, final_state):
        output_str = ' '.join(map(str, final_state))
        print(output_str)  # Changed to print for standard output