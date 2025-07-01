'''
This file contains the TrainCar and Train classes to manage toy train cars.
'''
class TrainCar:
    def __init__(self, car_number):
        self.car_number = car_number
        self.next_car = None
        self.prev_car = None
    def connect(self, car):
        self.next_car = car
        car.prev_car = self
    def disconnect(self):
        if self.next_car:
            self.next_car.prev_car = None
            self.next_car = None
class Train:
    def __init__(self):
        self.cars = {}
    def add_car(self, car_number):
        if car_number not in self.cars:
            self.cars[car_number] = TrainCar(car_number)
    def connect(self, x, y):
        self.add_car(x)
        self.add_car(y)
        self.cars[x].connect(self.cars[y])
    def disconnect(self, x, y):
        if x in self.cars and y in self.cars:
            self.cars[x].disconnect()
    def print_connected_component(self, x):
        if x not in self.cars:
            return []
        component = []
        current = self.cars[x]
        while current:
            component.append(current.car_number)
            current = current.next_car
        return component