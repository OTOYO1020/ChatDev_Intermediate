'''
Main entry point for the Snake Queue application.
'''
from snake_queue import SnakeQueue
def main():
    Q = int(input("Enter the number of queries: "))
    queue_manager = SnakeQueue()
    results = []
    for _ in range(Q):
        query = input().strip().split()
        query_type = int(query[0])
        if query_type == 1:
            length = int(query[1])
            queue_manager.add_snake(length)
        elif query_type == 2:
            queue_manager.remove_snake()
        elif query_type == 3:
            k = int(query[1])
            result = queue_manager.get_head_position(k)
            if result is not None:
                results.append(result)
            else:
                results.append("Invalid query for head position.")
        else:
            results.append("Invalid query type.")
    for result in results:
        print(result)
if __name__ == "__main__":
    main()