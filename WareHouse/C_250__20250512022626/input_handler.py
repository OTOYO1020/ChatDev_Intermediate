'''
Handles user input for the Ball Swapper application.
'''
class InputHandler:
    def get_input(self):
        N, Q = map(int, input().split())
        operations = [int(input()) for _ in range(Q)]
        return N, Q, operations