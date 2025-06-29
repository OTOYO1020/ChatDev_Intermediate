'''
Main application file for the color assignment program.
This program reads a sequence of integers and determines the minimum number of colors needed
based on the specified conditions.
'''
import sys
def calculate_colors(input_values):
    N = input_values[0]
    A = input_values[1:N+1]
    A_sorted = sorted(A)  # Sort without removing duplicates to maintain original sequence
    colors = 0
    last_color = -1
    for number in A_sorted:
        if number > last_color:
            colors += 1
            last_color = number
    return colors
def main():
    print("Please enter the number of integers followed by the integers themselves (e.g., '5 1 2 3 4 5'):")
    try:
        input_values = list(map(int, sys.stdin.read().strip().split()))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return
    # Check for empty input or N <= 0
    if not input_values or input_values[0] <= 0:
        print("No integers provided or N is zero. No colors can be assigned.")
        return
    colors = calculate_colors(input_values)
    print(colors)
if __name__ == "__main__":
    main()