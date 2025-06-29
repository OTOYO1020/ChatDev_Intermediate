'''
This file contains helper functions related to the GUI.
'''
import tkinter as tk
from tkinter import messagebox
def show_message(message):
    '''
    Displays a message box with the given message.
    Parameters:
        message (str): Message to display
    '''
    messagebox.showinfo("Message", message)