'''
Main entry point of the application.
'''
from input_handler import get_input
from set_logic import count_valid_sets
def main():
    M, N, sets = get_input()
    valid_count = count_valid_sets(M, N, sets)
    print(valid_count)
if __name__ == "__main__":
    main()