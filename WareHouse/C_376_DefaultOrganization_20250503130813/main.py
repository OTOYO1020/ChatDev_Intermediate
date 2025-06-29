'''
Main entry point of the ToyBox application.
'''
from input_handler import InputHandler
from output_handler import OutputHandler
def main():
    # Initialize input and output handlers
    input_handler = InputHandler()
    output_handler = OutputHandler()
    # Read the number of toys and boxes
    N = int(input("Enter the number of toys and boxes: "))
    # Check if N is valid
    if N <= 1:
        output_handler.display_result("Error:", "There must be at least 2 toys to have boxes.")
        return
    try:
        # Read the sizes of the toys
        A = input_handler.get_inputs(input("Enter toy sizes (comma-separated): "))
        # Read the sizes of the existing boxes
        B = input_handler.get_inputs(input("Enter box sizes (comma-separated): "), is_box=True)
    except ValueError as e:
        output_handler.display_result("Error:", str(e))
        return
    # Ensure that the input arrays are valid
    if len(B) == 0:
        output_handler.display_result("Error:", "Box sizes cannot be empty.")
        return
    # Check if the number of boxes is sufficient
    if N > len(B) + 1:
        output_handler.display_result("Error:", "Not enough boxes to accommodate all toys.")
        return
    # Sort the toys array to ensure proper placement in boxes
    A.sort()
    # Determine the maximum size of the toys
    max_toy_size = max(A)
    # Sort the array B in ascending order to facilitate the placement of toys
    B.sort()
    # Initialize a variable 'requiredBoxes' to count how many boxes are needed
    required_boxes = 0
    toy_index = 0  # Index to track the current toy
    # Iterate through the sorted array B and check how many toys can be placed in the existing boxes
    for box in B:
        if toy_index < len(A) and box >= A[toy_index]:  # Check if the box can fit the current toy
            required_boxes += 1  # Increment for each box used
            while toy_index < len(A) and box >= A[toy_index]:  # Place all toys that fit in this box
                toy_index += 1
    # Check if all toys can be accommodated
    if toy_index < len(A):  # If there are still toys left that couldn't be placed
        min_new_box_size = max_toy_size
        output_handler.display_result("Minimum box size needed:", min_new_box_size)
    else:
        output_handler.display_result("Result:", "All toys can be accommodated.")
if __name__ == "__main__":
    main()