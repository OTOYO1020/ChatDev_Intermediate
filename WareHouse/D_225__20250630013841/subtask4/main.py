'''
This file contains the main logic for managing toy train cars through standard input and output.
'''
import sys
from train import Train
def main():
    input_data = sys.stdin.read().strip().splitlines()
    first_line = input_data[0].split()
    N = int(first_line[0])  # Number of toy train cars
    Q = int(first_line[1])  # Number of queries
    train = Train()
    output = []
    for i in range(1, Q + 1):
        query = input_data[i].split()
        query_type = int(query[0])
        if query_type == 1:  # connect
            x, y = int(query[1]), int(query[2])
            train.connect(x, y)
        elif query_type == 2:  # disconnect
            x, y = int(query[1]), int(query[2])
            train.disconnect(x, y)
        elif query_type == 3:  # print connected component
            x = int(query[1])
            component = train.print_connected_component(x)
            output.append(" ".join(map(str, component)))
    # Print all outputs for query type 3
    for line in output:
        print(line)
if __name__ == "__main__":
    main()