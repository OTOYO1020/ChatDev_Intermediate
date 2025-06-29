'''
Contains the InputValidation class for validating user input.
'''
class InputValidation:
    def validate_input(self, N, M, edges):
        if not (1 <= N <= 100) or not (1 <= M <= 1000):
            return False
        if len(edges) != M:
            return False
        for u, v in edges:
            if not (1 <= u <= N) or not (1 <= v <= N):
                return False
        return True