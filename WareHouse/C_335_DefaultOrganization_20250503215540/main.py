'''
Main entry point for the Dragon Movement application.
'''
from dragon import Dragon
def main():
    # Read integers N and Q from standard input
    N, Q = map(int, input("Enter number of parts (N) and number of queries (Q): ").split())
    dragon = Dragon(N)
    for _ in range(Q):
        query = input("Enter query: ").strip().split()
        query_type = int(query[0])
        if query_type == 1:
            direction = query[1]
            dragon.move(direction)
        elif query_type == 2:
            part_number = int(query[1])
            position = dragon.get_position(part_number)
            print(f"Position of part {part_number}: {position}")
if __name__ == "__main__":
    main()