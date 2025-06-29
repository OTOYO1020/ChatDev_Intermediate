'''
Utility functions for handling input and output.
'''
def display_result(result, result_text):
    result_text.delete(1.0, END)
    result_text.insert(END, str(result))