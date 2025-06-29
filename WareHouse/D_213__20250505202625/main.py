'''
Main entry point for the City Journey application.
'''
class CityJourneyApp:
    def __init__(self):
        self.root = None
        self.start_button = None
        self.visited_sequence_label = None
        self.create_ui()
    def create_ui(self):
        import tkinter as tk
        self.root = tk.Tk()
        self.root.title("City Journey Simulation")
        self.start_button = tk.Button(self.root, text="Start Journey", command=self.open_input_dialog)
        self.start_button.pack(pady=20)
        self.visited_sequence_label = tk.Label(self.root, text="")
        self.visited_sequence_label.pack(pady=20)
    def open_input_dialog(self):
        from input_dialog import InputDialog
        dialog = InputDialog(self.root, self.start_journey)
    def start_journey(self, num_cities, roads):
        from journey_logic import JourneyLogic
        journey = JourneyLogic(num_cities)
        for road in roads:
            journey.add_road(road[0], road[1])
        visited_sequence = journey.simulate_journey()
        self.update_visited_sequence(visited_sequence)
    def update_visited_sequence(self, sequence):
        self.visited_sequence_label.config(text="Visited Sequence: " + " -> ".join(map(str, sequence)))
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = CityJourneyApp()
    app.run()