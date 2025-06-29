'''
Main application file for the query retrieval software.
'''
from query_handler import QueryHandler
def main():
    while True:
        try:
            Q = int(input("Enter the number of queries: "))  # Read the number of queries with a prompt
            if Q <= 0:
                raise ValueError("The number of queries must be a positive integer.")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid integer.")
    query_handler = QueryHandler()  # Initialize the query handler
    results = []  # List to store results for type 2 queries
    error_messages = []  # List to store error messages
    for _ in range(Q):
        query = input().strip().split()  # Read each query
        if len(query) < 2:  # Check if there are enough elements in the query
            error_messages.append("Error: Insufficient arguments for the query.")
            continue  # Skip to the next iteration
        try:
            query_type = int(query[0])  # First element is the query type
        except ValueError:
            error_messages.append("Error: Invalid query type. Please provide an integer value.")
            continue  # Skip to the next iteration
        if query_type == 1:
            try:
                x = int(query[1])  # Convert x to an integer before appending
                query_handler.add(x)  # Append value to the list
            except ValueError:
                error_messages.append("Invalid input for type 1 query. Please provide an integer value.")
        elif query_type == 2:
            if not query_handler.queries:  # Check if the list is empty
                error_messages.append("Error: No elements in the list")  # Append error message
            else:
                try:
                    k = int(query[1])  # Second element is the k value
                    result = query_handler.get_kth_from_end(k)  # Retrieve k-th value from the end
                    if isinstance(result, str) and "Error" in result:
                        error_messages.append(result)  # Append error message if any
                    else:
                        results.append(result)  # Store the result for output
                except ValueError:
                    error_messages.append("Invalid input for type 2 query. Please provide an integer value.")
                except IndexError:
                    error_messages.append("Error: k is greater than the number of elements in the list.")  # Handle IndexError
        else:
            error_messages.append("Error: Invalid query type. Please enter '1' or '2'.")  # Handle invalid query type
    # Print error messages if any
    for error in error_messages:
        print(error)
    # Print all results for type 2 queries at once
    if results:
        print("\n".join(map(str, results)))  
if __name__ == "__main__":
    main()