'''
Main application file for the Triangle Counter.
'''
from triangle_counter import count_triangles
def main():
    stick_lengths_input = input("Enter stick lengths (comma-separated): ")
    try:
        lengths = list(map(int, stick_lengths_input.split(',')))
        N = len(lengths)
        triangle_count = count_triangles(N, lengths)
        print(f"Number of triangles: {triangle_count}")
    except ValueError:
        print("Please enter valid integers separated by commas.")
if __name__ == "__main__":
    main()