'''
Module containing the App class for the GUI.
'''
from tkinter import Frame, Label, Entry, Button, Listbox, StringVar
from restaurant import RestaurantManager
class App:
    def __init__(self, root):  # Removed manager parameter
        self.root = root
        self.root.title("Restaurant Sorter")
        self.manager = RestaurantManager()  # Initialize manager here
        self.city_var = StringVar()
        self.score_var = StringVar()
        self.num_restaurants_var = StringVar()
        self.create_widgets()
    def create_widgets(self):
        frame = Frame(self.root)
        frame.pack(pady=10)
        Label(frame, text="Number of Restaurants:").grid(row=0, column=0)
        Entry(frame, textvariable=self.num_restaurants_var).grid(row=0, column=1)
        Button(frame, text="Set Number of Restaurants", command=self.set_number_of_restaurants).grid(row=0, column=2)
        Label(frame, text="City Name:").grid(row=1, column=0)
        Entry(frame, textvariable=self.city_var).grid(row=1, column=1)
        Label(frame, text="Score:").grid(row=2, column=0)
        Entry(frame, textvariable=self.score_var).grid(row=2, column=1)
        self.add_button = Button(frame, text="Add Restaurant", command=self.add_restaurant)
        self.add_button.grid(row=3, columnspan=2)
        Button(frame, text="Show Sorted IDs", command=self.display_sorted_ids).grid(row=4, columnspan=2)
        self.listbox = Listbox(self.root)
        self.listbox.pack(pady=10)
    def set_number_of_restaurants(self):
        try:
            max_restaurants = int(self.num_restaurants_var.get())
            if max_restaurants <= 0:
                print("Please enter a positive integer for the number of restaurants.")
                return
            self.manager.set_number_of_restaurants(max_restaurants)  # Reset the counter and clear restaurants
            self.listbox.delete(0, 'end')  # Clear the listbox
        except ValueError:
            print("Invalid number of restaurants. Please enter an integer value.")
    def add_restaurant(self):
        city = self.city_var.get()
        try:
            score = int(self.score_var.get())
            self.manager.add_restaurant(city, score)  # Use the manager to add the restaurant
            self.city_var.set("")
            self.score_var.set("")
        except ValueError:
            print("Invalid score. Please enter an integer value.")
    def display_sorted_ids(self):
        self.manager.sort_restaurants()
        sorted_ids = self.manager.get_sorted_ids()
        self.listbox.delete(0, 'end')
        for restaurant_id in sorted_ids:
            self.listbox.insert('end', restaurant_id)