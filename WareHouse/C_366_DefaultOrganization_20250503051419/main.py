'''
Main application file for managing a bag of integers through standard input/output.
'''
from bag import Bag  # Import the Bag class
def main():
    Q = int(input())
    bag = Bag()
    results = []
    for _ in range(Q):
        query = input().strip().split()
        query_type = int(query[0])
        try:
            if query_type == 1:
                x = int(query[1])
                bag.add(x)
            elif query_type == 2:
                x = int(query[1])
                bag.remove(x)  # Now raises an exception if x is not found
            elif query_type == 3:
                results.append(bag.count_unique())
            else:
                print("Invalid query type. Please enter 1, 2, or 3.")  # Handle invalid query types
        except ValueError:
            print("Invalid input. Please enter a valid integer for the query.")
        except KeyError as e:
            print(f"Error: {e}")  # Print the error message from KeyError
    for result in results:
        print(result)
if __name__ == "__main__":
    main()