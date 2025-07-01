'''
Main application file for character replacement without GUI.
'''
class MainApp:
    def replace_characters(self, input_string, operations):
        """
        Replace all occurrences of specified characters in the input string.
        Parameters:
        input_string (str): The original string to modify.
        operations (list of tuples): A list of character pairs (c, d) where
                                      c is replaced by d in the input_string.
        Returns:
        str: The modified string after all replacements.
        """
        for c, d in operations:
            input_string = input_string.replace(c, d)
        return input_string
if __name__ == "__main__":
    try:
        # Read inputs
        N, Q = map(int, input().split())
        S = input().strip()
        if len(S) != N:
            raise ValueError("The length of string S must be equal to N.")
        operations = []
        for _ in range(Q):
            c, d = input().strip().split()  # Expecting two characters
            if len(c) != 1 or len(d) != 1:
                raise ValueError("Each character pair must consist of exactly one character.")
            operations.append((c, d))
        app = MainApp()
        modified_string = app.replace_characters(S, operations)
        print(modified_string)
    except ValueError as e:
        print(f"Input error: {e}")