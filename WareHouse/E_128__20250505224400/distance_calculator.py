'''
Module for calculating distances based on roadworks and people's starting times.
'''
def calculate_distances(roadworks, people):
    # Sort roadworks based on the coordinate X_i
    roadworks.sort(key=lambda x: x[0])
    distances = []
    last_roadwork_coordinate = roadworks[-1][0] if roadworks else 0  # Get the last roadwork coordinate
    last_roadwork_end_time = roadworks[-1][2] if roadworks else 0  # Get the end time of the last roadwork
    for d in people:
        max_distance = 0  # Initialize to 0 to indicate no roadwork blocks
        for x, s, t in roadworks:
            if d < s:  # If the person starts before the roadwork
                max_distance = x  # They can walk to the roadwork
                break  # No need to check further roadworks
            elif s <= d < t:  # If the person starts during the roadwork
                max_distance = x  # They cannot walk past this roadwork
                break  # They are blocked
            elif d >= t:  # If the person starts after the roadwork has ended
                max_distance = max(max_distance, x)  # They can walk past this roadwork
        # If they start after all roadworks have ended
        if d > last_roadwork_end_time:
            max_distance = last_roadwork_coordinate  # Allow walking to the last roadwork coordinate
        distances.append(max_distance)  # Store the maximum distance for this person
    return distances