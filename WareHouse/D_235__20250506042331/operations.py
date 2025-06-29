'''
Module for performing operations on integers a and N.
'''
class Operations:
    def __init__(self, a, N):
        self.a = a
        self.N = N
        self.operations = 0
        self.x = 1
    def perform_operations(self):
        """
        Perform operations to reach the target number N by multiplying by a or manipulating digits.
        Returns the number of operations performed or -1 if N cannot be reached.
        """
        while self.x < self.N:  # Continue until x is less than N
            if self.x * self.a <= self.N:
                self.x *= self.a
                self.operations += 1
            elif self.x >= 10 and self.x % 10 != 0:
                self.x = int(str(self.x)[-1] + str(self.x)[:-1])
                self.operations += 1
            else:
                break  # Exit if no operations can be performed
        # Final check if we reached N after the loop
        if self.x == self.N:
            return self.operations
        else:
            return -1  # Return -1 if x exceeds N without reaching N