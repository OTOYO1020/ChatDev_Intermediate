'''
InputValidation class to validate user inputs for the application.
'''
class InputValidation:
    def validate_inputs(self, N, A, W):
        if not isinstance(N, int) or N <= 0:
            return False
        if len(A) != N or len(W) != N:
            return False
        if not all(isinstance(x, int) for x in A) or not all(isinstance(x, int) for x in W):
            return False
        return True