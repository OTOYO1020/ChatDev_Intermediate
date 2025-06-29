'''
Module to define the TrainInfo class for handling train information.
'''
class TrainInfo:
    def __init__(self, l_i, d_i, k_i, c_i, A_i, B_i):
        self.l_i = l_i  # Length of the train
        self.d_i = d_i  # Departure station
        self.k_i = k_i  # Arrival station
        self.c_i = c_i  # Departure time
        self.A_i = A_i  # Arrival time at the departure station
        self.B_i = B_i  # Arrival time at the arrival station