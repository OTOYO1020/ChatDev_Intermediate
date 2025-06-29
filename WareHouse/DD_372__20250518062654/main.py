'''
Main file to run the Building Visibility application.
'''
from typing import List
from building_visibility import count_visible_buildings
def main():
    try:
        n = int(input("Enter number of buildings (N): "))
        heights = list(map(int, input("Enter heights of buildings (comma-separated): ").split(',')))
        if len(heights) != n:
            raise ValueError("Number of heights must match N.")
        result = count_visible_buildings(n, heights)
        print(result)
    except ValueError as ve:
        print(f"Value Error: {str(ve)}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()