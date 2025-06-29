'''
Main entry point for the building selection application.
'''
from collections import defaultdict
def calculate_max_buildings(N, heights):
    """
    Calculate the maximum number of buildings that can be selected based on their heights.
    Parameters:
    N (int): The number of buildings.
    heights (list): A list of integers representing the heights of the buildings.
    Returns:
    int: The maximum count of buildings that can be selected.
    """
    max_count = 1  # Initialize max_count to 1 since at least one building can be chosen
    height_dict = defaultdict(list)  # Dictionary to store indices of buildings by height
    # Populate the dictionary with indices of each building height
    for index, height in enumerate(heights):
        height_dict[height].append(index)
    # Iterate through each unique height
    for indices in height_dict.values():
        if len(indices) < 2:
            continue  # If less than two buildings of this height, skip to next
        # Check all pairs of indices to determine possible intervals
        for i in range(len(indices)):
            for j in range(i + 1, len(indices)):
                interval = indices[j] - indices[i]  # Calculate the interval
                count = 2  # Start with the two buildings at indices[i] and indices[j]
                next_index = indices[j] + interval  # Calculate the next index
                # Count how many buildings can be selected with this interval
                while True:
                    if next_index < N and heights[next_index] == heights[indices[i]]:
                        count += 1
                        next_index += interval
                    else:
                        break
                # Update max_count if the current count exceeds it
                max_count = max(max_count, count)
    return max_count
if __name__ == "__main__":
    try:
        N = int(input("Enter the number of buildings (N): "))
        heights_input = input("Enter the heights (comma-separated integers): ")
        heights = list(map(int, heights_input.split(',')))  # Convert input to a list of integers
        if N != len(heights):
            raise ValueError("Number of buildings does not match the length of heights.")
        max_count = calculate_max_buildings(N, heights)
        print(max_count)
    except ValueError as e:
        print(f"Error: {str(e)}. Please ensure you enter valid integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")