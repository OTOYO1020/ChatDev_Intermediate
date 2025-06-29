'''
Module to check if the desired hat configuration can be achieved from the current configuration.
'''
class HatColorChecker:
    def can_achieve(self, current, desired):
        # Check if both strings are permutations of each other
        if sorted(current) == sorted(desired):
            return "YES"
        return "NO"