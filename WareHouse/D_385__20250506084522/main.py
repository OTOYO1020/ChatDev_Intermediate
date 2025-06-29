'''
Main application file that handles the Santa's house tracking logic.
'''
def move_and_track(direction, distance, current_x, current_y, visited_houses, houses):
    # Track all intermediate positions based on the direction and distance
    if direction == 'U':
        for y in range(current_y, current_y + distance + 1):
            if (current_x, y) in houses:
                visited_houses.add((current_x, y))
        current_y += distance
    elif direction == 'D':
        for y in range(current_y, current_y - distance - 1, -1):
            if (current_x, y) in houses:
                visited_houses.add((current_x, y))
        current_y -= distance
    elif direction == 'L':
        for x in range(current_x, current_x - distance - 1, -1):
            if (x, current_y) in houses:
                visited_houses.add((x, current_y))
        current_x -= distance
    elif direction == 'R':
        for x in range(current_x, current_x + distance + 1):
            if (x, current_y) in houses:
                visited_houses.add((x, current_y))
        current_x += distance
    # Check the final position after the movement
    if (current_x, current_y) in houses:
        visited_houses.add((current_x, current_y))
    return current_x, current_y
def main():
    try:
        N = int(input("Enter the number of houses: "))
        M = int(input("Enter the number of movements: "))
    except ValueError:
        print("Error: Please enter valid integers for the number of houses and movements.")
        return
    houses = []
    for _ in range(N):
        try:
            house_coordinates = tuple(map(int, input("Enter house coordinates (x,y): ").split(',')))
            if len(house_coordinates) != 2:
                raise ValueError
            houses.append(house_coordinates)
        except ValueError:
            print("Error: Please enter valid coordinates in the format 'x,y'.")
            return
    try:
        S_x, S_y = map(int, input("Enter Santa's starting position (x,y): ").split(','))
    except ValueError:
        print("Error: Please enter valid integers for Santa's starting position.")
        return
    visited_houses = set()
    current_x, current_y = S_x, S_y
    for _ in range(M):
        movement_input = input("Enter movement (D,C): ").split(',')
        if len(movement_input) != 2:
            print("Error in input: Movement input must be in the format 'D,C'")
            return
        direction, distance_str = movement_input
        try:
            distance = int(distance_str)
            if direction not in ['U', 'D', 'L', 'R'] or distance < 0:
                raise ValueError
        except ValueError:
            print("Error in input: Invalid movement direction or distance")
            return
        # Update current position based on the direction and track all positions passed
        current_x, current_y = move_and_track(direction, distance, current_x, current_y, visited_houses, houses)
    print(f"Final Position: ({current_x}, {current_y})")
    print(f"Distinct Houses Visited: {len(visited_houses)}")
if __name__ == "__main__":
    main()