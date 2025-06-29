'''
Contains functions for rotating and translating points, and comparing sets of points.
'''
import math
def rotate_point(point, angle):
    '''
    Rotates a point by a specified angle.
    '''
    x, y = point
    radians = math.radians(angle)
    new_x = x * math.cos(radians) - y * math.sin(radians)
    new_y = x * math.sin(radians) + y * math.cos(radians)
    return (new_x, new_y)
def translate_point(point, q, r):
    '''
    Translates a point by specified values.
    '''
    x, y = point
    return (x + q, y + r)
def transform_and_compare(S, T):
    '''
    Transforms points in S and compares them with points in T.
    '''
    for angle in range(0, 360):  # Iterate through all angles from 0 to 359
        rotated_S = [rotate_point(point, angle) for point in S]
        for t_point in T:  # Iterate through each point in T for translation
            translation_x = t_point[0] - rotated_S[0][0]
            translation_y = t_point[1] - rotated_S[0][1]
            translated_S = [translate_point(point, translation_x, translation_y) for point in rotated_S]
            # Sort both lists before comparison
            if sorted(translated_S) == sorted(T):  # Use sorted lists for comparison
                return True
    return False