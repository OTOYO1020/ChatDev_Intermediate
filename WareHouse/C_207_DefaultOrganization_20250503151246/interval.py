'''
Module containing the Interval class and intersection logic.
'''
class Interval:
    def __init__(self, t, l, r):
        '''
        Initialize an Interval object.
        Parameters:
            t (int): Type of interval (1 to 4).
            l (int): Left endpoint of the interval.
            r (int): Right endpoint of the interval.
        '''
        self.t = t
        self.l = l
        self.r = r
    def intersects(self, other):
        '''
        Check if this interval intersects with another interval.
        Parameters:
            other (Interval): The other interval to check against.
        Returns:
            bool: True if the intervals intersect, False otherwise.
        '''
        if self.t == 1:  # [l, r]
            return self._intersects_closed(other)
        elif self.t == 2:  # [l, r)
            return self._intersects_left_closed(other)
        elif self.t == 3:  # (l, r]
            return self._intersects_right_closed(other)
        elif self.t == 4:  # (l, r)
            return self._intersects_open(other)
        else:
            raise ValueError("Invalid interval type.")
    def _intersects_closed(self, other):
        '''
        Check intersection for closed interval [l, r].
        Parameters:
            other (Interval): The other interval to check against.
        Returns:
            bool: True if the intervals intersect, False otherwise.
        '''
        return not (self.r < other.l or other.r < self.l)
    def _intersects_left_closed(self, other):
        '''
        Check intersection for left closed interval [l, r).
        Parameters:
            other (Interval): The other interval to check against.
        Returns:
            bool: True if the intervals intersect, False otherwise.
        '''
        return not (self.r < other.l or other.r <= self.l)
    def _intersects_right_closed(self, other):
        '''
        Check intersection for right closed interval (l, r].
        Parameters:
            other (Interval): The other interval to check against.
        Returns:
            bool: True if the intervals intersect, False otherwise.
        '''
        return not (self.r <= other.l or other.r < self.l)
    def _intersects_open(self, other):
        '''
        Check intersection for open interval (l, r).
        Parameters:
            other (Interval): The other interval to check against.
        Returns:
            bool: True if the intervals intersect, False otherwise.
        '''
        return not (self.r <= other.l or other.r <= self.l)