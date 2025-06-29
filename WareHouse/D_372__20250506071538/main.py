'''
Main application file for the Building Validity Counter.
'''
from building_counter import BuildingCounter
def main():
    try:
        n = int(input("Enter the number of buildings: "))
        heights = list(map(int, input("Enter the heights of the buildings (space-separated): ").split()))
        if len(heights) != n:
            raise ValueError("Number of heights does not match the number of buildings.")
        counter = BuildingCounter(heights)
        result = counter.count_valid_buildings()
        for count in result:  # Print all counts
            print(count)
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()