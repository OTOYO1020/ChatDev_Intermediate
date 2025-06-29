'''
Main application for managing pigeons and nests through standard input and output.
'''
def main():
    '''
    Main function to handle input and output for pigeon management.
    Reads the number of pigeons and nests, processes queries, and outputs results.
    '''
    import sys
    from pigeon_manager import PigeonManager  # Importing PigeonManager
    input = sys.stdin.read
    data = input().splitlines()
    # Read N and Q
    N, Q = map(int, data[0].split())
    manager = PigeonManager(N, N)  # Initialize with N pigeons and N nests
    results = []
    for i in range(1, Q + 1):
        query = list(map(int, data[i].split()))
        if query[0] == 1:  # Move pigeon
            _, P, H = query
            manager.move_pigeon(P, H)
        elif query[0] == 2:  # Count nests with multiple pigeons
            results.append(manager.count_multiple_pigeons())
    # Output results for all '2' queries
    print('\n'.join(map(str, results)))
if __name__ == "__main__":
    main()