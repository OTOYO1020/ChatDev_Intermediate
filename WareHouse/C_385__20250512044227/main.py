'''
Main application file for the Illumination application.
'''
from illumination import maxIlluminatedBuildings
def main():
    try:
        N = int(input("Enter number of buildings (N): "))
        heights = list(map(int, input("Enter heights of buildings (comma-separated): ").split(',')))
        if len(heights) != N:
            raise ValueError("Number of heights must match N.")
        max_count = maxIlluminatedBuildings(N, heights)
        print(f"Maximum illuminated buildings: {max_count}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()