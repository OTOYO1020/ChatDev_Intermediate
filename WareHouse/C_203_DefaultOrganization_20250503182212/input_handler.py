'''
Input handling module for Taro's travel distance calculator.
'''
class InputHandler:
    def get_input(self):
        while True:
            try:
                n = int(input("Enter number of friends (N): "))
                k = int(input("Enter initial money (K): "))
                friends_data = input("Enter friends' data (A_i, B_i) separated by semicolons (e.g., '1,100; 2,200'): ").strip().split(';')
                friends = []
                for data in friends_data:
                    data = data.strip()  # Trim spaces
                    if not data:  # Check for empty input
                        raise ValueError("Friend data cannot be empty. Please enter in the format 'A_i,B_i'.")
                    # Check if the data is in the correct format
                    if ',' not in data or data.count(',') != 1:
                        raise ValueError(f"Invalid format for friend data: '{data}'. Expected format is 'A_i,B_i'.")
                    try:
                        a, b = map(int, data.split(','))
                    except ValueError:
                        raise ValueError(f"Invalid integers in friend data: '{data}'. Please ensure both A_i and B_i are integers.")
                    friends.append((a, b))
                if len(friends) != n:
                    raise ValueError(f"Expected {n} friends, but got {len(friends)}. Please enter the correct number of friends.")
                return n, k, friends
            except ValueError as e:
                print(f"Invalid input: {e}. Please ensure you enter integers in the correct format.")
    def validate_input(self, n, k, friends):
        if n <= 0 or k < 0:
            raise ValueError("N must be greater than 0 and K must be non-negative.")
        for a, b in friends:
            if a < 0 or b < 0:
                raise ValueError("Village number and yen amount must be non-negative.")