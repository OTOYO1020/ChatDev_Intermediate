'''
This file contains the TrainCar and Train classes to manage toy train cars.
'''
class TrainCar:
    def __init__(self, car_number):
        self.car_number = car_number
        self.next_car = None
        self.prev_car = None
    def connect(self, car):
        '''
        Connects this car to the next car.
        Parameters:
        car (TrainCar): The car to connect to.
        '''
        self.next_car = car
        car.prev_car = self
    def disconnect(self):
        '''
        Disconnects the next car from this car.
        '''
        if self.next_car:
            self.next_car.prev_car = None
            self.next_car = None
class Train:
    def __init__(self):
        self.cars = {}
    def add_car(self, car_number):
        '''
        Adds a new car to the train if it does not already exist.
        Parameters:
        car_number (int): The number of the car to add.
        '''
        if car_number not in self.cars:
            self.cars[car_number] = TrainCar(car_number)
    def connect(self, x, y):
        '''
        Connects car y to the rear of car x.
        Parameters:
        x (int): The number of the first car.
        y (int): The number of the second car.
        '''
        self.add_car(x)
        self.add_car(y)
        self.cars[x].connect(self.cars[y])
    def disconnect(self, x, y):
        '''
        Disconnects car y from the rear of car x.
        Parameters:
        x (int): The number of the first car.
        y (int): The number of the second car.
        '''
        if x in self.cars and y in self.cars:
            # Traverse to find if y is connected to x
            current = self.cars[x]
            while current:
                if current.next_car == self.cars[y]:
                    current.next_car = self.cars[y].next_car
                    if self.cars[y].next_car:
                        self.cars[y].next_car.prev_car = current
                    self.cars[y].prev_car = None  # Clear the previous reference of y
                    self.cars[y].next_car = None  # Ensure y does not point to any other car
                    return
                current = current.next_car
            print(f"Car {y} is not connected to car {x}.")
        else:
            print(f"One or both cars do not exist: {x}, {y}.")
    def print_connected_component(self, x):
        '''
        Retrieves the list of car numbers in the connected component containing car x.
        Parameters:
        x (int): The number of the car to find the connected component for.
        Returns:
        list: A list of car numbers in the connected component.
        '''
        if x not in self.cars:
            print(f"Car {x} does not exist.")
            return []  # Return an empty list for non-existent car
        component = []
        current = self.cars[x]
        while current:
            component.append(current.car_number)
            current = current.next_car
        return component