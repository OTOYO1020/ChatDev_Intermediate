'''
Computation logic for finding the smallest integer X that satisfies the given conditions.
'''
class Computation:
    '''
    Class that contains methods to compute the smallest integer X.
    '''
    def find_x(self, n):
        '''
        Finds the smallest integer X such that X = a^3 + a^2b + ab^2 + b^3 for non-negative integers a and b.
        Optimized to reduce unnecessary iterations.
        '''
        x = n
        while True:
            found = False
            for a in range(int(x**(1/3)) + 1):
                a_cubed = a ** 3
                if a_cubed > x:
                    break
                for b in range(int((x - a_cubed)**(1/3)) + 1):
                    b_cubed = b ** 3
                    if a_cubed + b_cubed > x:
                        break
                    remainder = x - (a_cubed + b_cubed)
                    if remainder >= 0:
                        # Check if remainder can be expressed as a^2 * b + a * b^2
                        for b_check in range(int(remainder**0.5) + 1):
                            if b_check == 0:
                                continue  # Avoid division by zero
                            a_check = remainder // (b_check + 1)  # Calculate a based on b
                            if remainder == a_check**2 * b_check + a_check * b_check**2:
                                found = True
                                break
                        if found:
                            break
                if found:
                    return x
            x += 1