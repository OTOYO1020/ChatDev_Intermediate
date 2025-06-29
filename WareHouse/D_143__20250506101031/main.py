'''
Main entry point for the Triangle Counter application.
'''
def count_triangles(stick_lengths):
    """
    Count the number of valid triangles that can be formed with the given stick lengths.
    Parameters:
    stick_lengths (list): A list of integers representing the lengths of the sticks.
    Returns:
    int: The count of valid triangles.
    """
    triangle_count = 0
    N = len(stick_lengths)
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                a = stick_lengths[i]
                b = stick_lengths[j]
                c = stick_lengths[k]
                if a < b + c and b < c + a and c < a + b:
                    triangle_count += 1
    return triangle_count
def validate_input_lengths(lengths, expected_count):
    """
    Validate that the input lengths are positive integers and match the expected count.
    Parameters:
    lengths (list): A list of strings representing the lengths of the sticks.
    expected_count (int): The expected number of lengths.
    Returns:
    tuple: A boolean indicating validity and the list of integers if valid.
    """
    if len(lengths) != expected_count:
        return False, None
    try:
        lengths = [int(length) for length in lengths]
        if any(length <= 0 for length in lengths):
            return False, None
    except ValueError:
        return False, None
    return True, lengths
if __name__ == "__main__":
    while True:
        try:
            N = int(input("Enter the number of sticks (positive integer): "))
            if N <= 0:
                print("Error: The number of sticks must be a positive integer.")
                continue
            stick_lengths_input = input("Enter the lengths of the sticks (space-separated positive integers): ")
            stick_lengths = list(map(str.strip, stick_lengths_input.split()))
            is_valid, stick_lengths = validate_input_lengths(stick_lengths, N)
            if not is_valid:
                print(f"Error: You must enter exactly {N} positive integer lengths (e.g., '3 4 5').")
                continue
            # Ensure stick_lengths are integers before passing to count_triangles
            result = count_triangles([int(length) for length in stick_lengths])
            print("Number of valid triangles:", result)
            break  # Exit the loop after successful execution
        except ValueError:
            print("Error: Please enter a valid integer value for the number of sticks.")