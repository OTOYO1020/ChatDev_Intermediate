'''
Module to handle user input for the expected value calculator.
'''
class InputHandler:
    def get_input(self, n_str, k_str, a_str):
        try:
            N = int(n_str)
            K = int(k_str)
            A = list(map(int, a_str.split()))
            if len(A) != N:
                raise ValueError("Length of A must be equal to N.")
            return N, K, A
        except ValueError as e:
            print(f"Input error: {e}")
            return None, None, None