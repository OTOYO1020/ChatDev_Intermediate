'''
Module to handle the logic for counting sock pairs.
'''
class SockPairCounter:
    def __init__(self):
        pass
    def calculate_pairs(self, N, colors):
        '''
        Calculate the maximum number of pairs that can be formed from the given sock colors.
        Parameters:
        N (int): The number of socks.
        colors (list): A list of integers representing the colors of the socks.
        Returns:
        int: The maximum number of pairs that can be formed.
        '''
        color_count = {}
        for color in colors:
            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1
        max_pairs = sum(count // 2 for count in color_count.values())
        return max_pairs
    def run(self):
        '''
        Run the sock pair counting application. This method handles user input and output.
        It prompts the user to enter the number of socks and their colors, validates the input,
        and displays the maximum number of pairs that can be formed.
        '''
        try:
            N = int(input("Enter the number of socks: "))
            if N <= 0:  # Check if the number of socks is valid
                raise ValueError("The number of socks must be greater than zero.")
            colors_input = input("Enter sock colors (comma-separated integers): ").strip()
            if not colors_input:  # Check if the input is empty
                raise ValueError("Sock colors input cannot be empty.")
            colors = []
            for color in colors_input.split(','):
                try:
                    colors.append(int(color.strip()))  # Convert each color to an integer
                except ValueError:
                    raise ValueError("All sock colors must be valid integers.")
            if len(colors) != N:
                raise ValueError("The number of colors must match the number of socks.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter valid integers.")
            return  # Exit the method if input is invalid
        max_pairs = self.calculate_pairs(N, colors)
        print(f"Maximum pairs: {max_pairs}")