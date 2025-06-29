'''
Main application file for the Potato Packing Application.
'''
from potato_box import PotatoBox
from utils import validate_input
def main():
    # Read integers N and Q from standard input
    N, Q = map(int, input().split())
    # Read weights of potatoes
    weights = list(map(int, input().split()))  # Changed to space-separated input
    # Read the weight threshold (X)
    threshold = int(input())
    if validate_input(weights, threshold):
        potato_box = PotatoBox(weights, threshold)
        potato_box.pack_potatoes()
        # Process Q queries
        for _ in range(Q):
            query = int(input())
            result = potato_box.get_box_count(query)
            if result == -1:
                print("Box does not exist.")
            else:
                print(result)
if __name__ == "__main__":
    main()