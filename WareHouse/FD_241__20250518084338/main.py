'''
Main application file for the Takahashi movement simulation.
'''
from movement import min_moves
def main():
    # Input parsing
    try:
        H, W, N = map(int, input("Enter grid height (H), width (W), and number of obstacles (N): ").split())
        s_x, s_y = map(int, input("Enter Start (s_x, s_y): ").split())
        g_x, g_y = map(int, input("Enter Goal (g_x, g_y): ").split())
        # Validate starting and goal positions
        if not (1 <= s_x <= W and 1 <= s_y <= H):
            print("Input Error: Starting position is out of grid boundaries.")
            return
        if not (1 <= g_x <= W and 1 <= g_y <= H):
            print("Input Error: Goal position is out of grid boundaries.")
            return
        obstacles = []
        if N > 0:
            obstacles_input = input("Enter obstacles (X1 Y1, X2 Y2, ...): ")
            obstacle_pairs = obstacles_input.split(',')
            if len(obstacle_pairs) != N:
                print(f"Input Error: Expected {N} obstacle coordinates, but got {len(obstacle_pairs)}.")
                return
            for obs in obstacle_pairs:
                try:
                    x, y = map(int, obs.strip().split())
                    if not (1 <= x <= W and 1 <= y <= H):
                        print(f"Input Error: Obstacle ({x}, {y}) is out of grid boundaries.")
                        return
                    obstacles.append((x, y))
                except ValueError:
                    print("Input Error: Please enter valid obstacle coordinates in the format 'X Y'.")
                    return
        # Check if starting or goal positions are obstacles
        if (s_x, s_y) in obstacles:
            print("Input Error: Starting position cannot be an obstacle.")
            return
        if (g_x, g_y) in obstacles:
            print("Input Error: Goal position cannot be an obstacle.")
            return
        result = min_moves(s_x, s_y, g_x, g_y, obstacles, grid_width=W, grid_height=H)
        print(f"Minimum Moves: {result}")
    except ValueError:
        print("Input Error: Please enter valid integers.")
if __name__ == "__main__":
    main()