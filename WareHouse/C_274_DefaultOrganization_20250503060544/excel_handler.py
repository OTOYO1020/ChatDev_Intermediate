'''
Excel handler for reading amoeba data from Excel files.
'''
import pandas as pd
class ExcelHandler:
    def __init__(self, filename):
        self.filename = filename
    def read_excel(self):
        # Read the Excel file and return the data as a list
        df = pd.read_excel(self.filename)
        # Assuming the data is in the first column
        return df.iloc[:, 0].tolist()