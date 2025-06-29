'''
Module to handle bean data processing for the Bean Deliciousness Calculator.
'''
from collections import defaultdict
class BeanHandler:
    '''
    Class to manage bean deliciousness values by color.
    '''
    def __init__(self):
        self.color_map = defaultdict(list)
    def add_bean(self, deliciousness, color):
        '''
        Adds a bean's deliciousness value to the corresponding color list.
        '''
        self.color_map[color].append(deliciousness)
    def compute_max_min_deliciousness(self):
        '''
        Computes the maximum of the minimum deliciousness values for each color.
        Returns None if no beans have been added.
        '''
        min_deliciousness = []
        for deliciousness_list in self.color_map.values():
            if deliciousness_list:  # Ensure the list is not empty
                min_deliciousness.append(min(deliciousness_list))
        return max(min_deliciousness) if min_deliciousness else None