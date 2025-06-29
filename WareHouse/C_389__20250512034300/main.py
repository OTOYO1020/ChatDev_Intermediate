'''
Main entry point for the application.
'''
from query_processor import QueryProcessor
def main():
    Q = int(input("Enter number of queries: "))
    if Q <= 0:
        raise ValueError("The number of queries must be a positive integer.")
    queries = []
    for _ in range(Q):
        query = tuple(map(int, input("Enter query: ").split()))
        queries.append(query)
    processor = QueryProcessor()
    results = processor.process_queries(Q, queries)
    print(results)
if __name__ == "__main__":
    main()