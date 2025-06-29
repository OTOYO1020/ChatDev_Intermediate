'''
Module for counting operations on a sequence of integers.
'''
import heapq
class OperationCounter:
    '''
    Class to count operations on a list of integers.
    '''
    def __init__(self, numbers):
        self.numbers = numbers
    def count_operations(self):
        '''
        Counts the number of operations needed to reduce the list to one positive integer.
        '''
        operation_count = 0
        # Create a max-heap (invert values for max-heap behavior)
        max_heap = [-num for num in self.numbers]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)  # Get the largest
            second = -heapq.heappop(max_heap)  # Get the second largest
            # Decrement both numbers
            first -= 1
            second -= 1
            operation_count += 1  # Increment operation count
            # Push back only if they are still positive
            if first > 0:
                heapq.heappush(max_heap, -first)
            if second > 0:
                heapq.heappush(max_heap, -second)
        return operation_count