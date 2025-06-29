class Data:
    def __init__(self):
        self.file_path = "data.txt"
        self.data = None
    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                self.data = file.read()
                return self.data
        except FileNotFoundError:
            return None
    def save_data(self, data):
        try:
            with open(self.file_path, 'w') as file:
                file.write(data)
                file.flush()
        except IOError:
            pass