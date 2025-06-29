'''
Handles user input for points.
'''
class InputHandler:
    def get_points(self, N):
        points = []
        try:
            print(f"Enter {N} points (X, Y) separated by spaces:")
            coords = input().split()
            if len(coords) != N * 2:
                raise ValueError("Number of coordinates does not match N.")
            for i in range(N):
                x = int(coords[i * 2].strip())
                y = int(coords[i * 2 + 1].strip())
                points.append((x, y))
            return points
        except ValueError as e:
            raise ValueError(f"Invalid input: {e}")