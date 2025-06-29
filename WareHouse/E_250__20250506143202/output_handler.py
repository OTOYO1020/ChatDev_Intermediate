'''
Manages output display to the user.
'''
import sys
class OutputHandler:
    def display_results(self, results):
        # Print results to standard output
        sys.stdout.write("\n".join(results) + "\n")