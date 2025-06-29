'''
Main entry point for the Max Satisfaction application.
'''
import sys
from satisfaction import max_satisfaction
def main():
    # Read input from standard input
    input_data = sys.stdin.read().strip().splitlines()
    N = int(input_data[0])
    flavors = list(map(int, input_data[1].split(',')))
    deliciousness = list(map(int, input_data[2].split(',')))
    # Validate input lengths
    if len(flavors) != N or len(deliciousness) != N:
        raise ValueError("The number of flavors and deliciousness must match N.")
    # Calculate maximum satisfaction
    max_satis = max_satisfaction(N, flavors, deliciousness)
    # Print the maximum satisfaction value
    print(max_satis)
if __name__ == "__main__":
    main()