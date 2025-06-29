'''
Module for handling input operations for the main application.
'''
def insert_left(A, i):
    '''
    Inserts the integer i to the left of the last element in list A.
    This means i should be added before the last element of the list.
    '''
    A.insert(len(A) - 1, i)  # Insert before the last element to maintain order.
def append_right(A, i):
    '''
    Appends the integer i to the right of the last element in list A.
    '''
    A.append(i)