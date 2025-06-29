'''
This file is used to run the software without the GUI.
'''
from data import Data
# Create an instance of the Data class
data = Data()
# Load the data from a file
data.load_data("input.txt")
# Process the data
result = data.process_data()
# Save the result to a file
data.save_data("output.txt")