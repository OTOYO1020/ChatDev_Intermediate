'''
Module to generate palindromes and count valid ones.
'''
class PalindromeGenerator:
    MOD = 998244353
    def __init__(self):
        pass
    def generate_palindrome(self, n, s):
        '''
        Generate valid palindromes based on the input string and count them.
        Parameters:
        n (int): Length of the string S.
        s (str): The input string to compare against.
        Returns:
        int: The count of valid palindromes modulo MOD.
        '''
        half_length = (n + 1) // 2
        first_half = list(s[:half_length])  # Convert to list for mutability
        count = 0
        while True:
            # Generate the palindrome from the first half
            palindrome = first_half + first_half[-(n // 2):][::-1]
            palindrome_str = ''.join(palindrome)
            # Check if the generated palindrome is equal to S
            if palindrome_str == s:
                count += 1
            elif palindrome_str < s:
                count += self.count_valid_palindromes(first_half, s[:half_length])
            # Increment the first half to find the next valid palindrome
            if not self.increment_first_half(first_half):
                break  # No more valid increments possible
        return count % self.MOD
    def count_valid_palindromes(self, x, s):
        '''
        Count the number of valid palindromes that can be formed based on the first half.
        Parameters:
        x (list): The first half of the palindrome.
        s (str): The string to compare against.
        Returns:
        int: The count of valid palindromes modulo MOD.
        '''
        count = 1
        for i in range(len(x)):
            if x[i] < s[i]:
                count *= 26 ** (len(x) - i - 1)
                break
            elif x[i] > s[i]:
                count = 0  # No valid palindromes can be formed if x is greater than s
                break
        return count % self.MOD
    def increment_first_half(self, first_half):
        '''
        Increment the first half of the palindrome.
        Parameters:
        first_half (list): The current first half of the palindrome.
        Returns:
        bool: True if increment was successful, False if no more valid increments are possible.
        '''
        for i in range(len(first_half) - 1, -1, -1):
            if first_half[i] < 'z':
                first_half[i] = chr(ord(first_half[i]) + 1)
                return True  # Successfully incremented
            else:
                first_half[i] = 'a'  # Reset to 'a' and carry over
        # Check if all characters are 'a' after reset
        return not any(c != 'a' for c in first_half)  # Return True if all are 'a', indicating no more increments possible