'''
Main application file for the Potato Packing application.
'''
import sys
from utils import count_potatoes_in_boxes
def main():
    '''
    Main function to handle input and output for the Potato Packing application.
    '''
    input_data = sys.stdin.read().strip().splitlines()
    N = int(input_data[0])
    W = list(map(int, input_data[1].split(',')))
    X = int(input_data[2])
    Q = int(input_data[3])
    K = list(map(int, input_data[4].split(',')))
    if len(W) != N:
        raise ValueError("The number of weights must match N.")
    potatoes_in_boxes = count_potatoes_in_boxes(N, W, X, Q, K)
    print("Results:", ", ".join(map(str, potatoes_in_boxes)))
if __name__ == "__main__":
    main()