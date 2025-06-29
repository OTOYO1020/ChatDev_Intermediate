'''
Module to generate lunlun numbers.
'''
from collections import deque
class LunlunNumberGenerator:
    '''
    Class to generate lunlun numbers.
    '''
    def is_lunlun_number(self, number):
        '''
        Checks if a number is a lunlun number.
        '''
        str_num = str(number)
        for i in range(len(str_num) - 1):
            if abs(int(str_num[i]) - int(str_num[i + 1])) > 1:
                return False
        return True
    def generate_lunlun_numbers(self, k):
        '''
        Generates the first K lunlun numbers using a breadth-first search approach.
        '''
        lunlun_numbers = []
        queue = deque(range(1, 10))  # Start with single-digit lunlun numbers
        while len(lunlun_numbers) < k:
            current_number = queue.popleft()
            lunlun_numbers.append(current_number)
            last_digit = current_number % 10
            # Generate next lunlun numbers by appending last_digit-1, last_digit, last_digit+1
            for next_digit in (last_digit - 1, last_digit, last_digit + 1):
                if 0 <= next_digit <= 9:  # Ensure the digit is valid
                    new_number = current_number * 10 + next_digit
                    queue.append(new_number)
        return lunlun_numbers  # Return the entire list of lunlun numbers